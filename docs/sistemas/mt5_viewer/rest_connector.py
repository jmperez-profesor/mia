"""
Conector REST contra el backend Windows (api.py).
Misma interfaz que WineMT5Connector para que app.py no cambie.
Uso: MT5_API_URL=http://IP_WINDOWS:8000 python3 app.py
"""

import threading
import time
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Callable, Dict, List, Optional

import requests

ConnectionState = Enum(
    "ConnectionState", ["DISCONNECTED", "CONNECTING", "CONNECTED", "ERROR"]
)


@dataclass
class TradeEvent:
    tipo: str = ""
    simbolo: str = ""
    tipo_operacion: str = ""
    volumen: float = 0.0
    precio: float = 0.0
    stop_loss: float = 0.0
    take_profit: float = 0.0
    profit: float = 0.0
    commission: float = 0.0
    swap: float = 0.0
    saldo: float = 0.0
    equity: float = 0.0
    margin: float = 0.0
    margin_free: float = 0.0
    timestamp: datetime = datetime.now()
    ticket: int = 0
    comentario: str = ""
    estado: str = ""


@dataclass
class AccountInfo:
    login: int = 0
    nombre: str = ""
    servidor: str = ""
    compania: str = ""
    saldo: float = 0.0
    equity: float = 0.0
    margin: float = 0.0
    margin_free: float = 0.0
    margin_level: float = 0.0
    profit: float = 0.0
    gross_profit: float = 0.0
    gross_loss: float = 0.0
    commission: float = 0.0
    swap: float = 0.0
    leverage: int = 0
    balance: float = 0.0
    credito: float = 0.0
    estado: str = ""


class RestMT5Connector:
    """Un conector por cuenta, todos contra el mismo backend HTTP."""

    def __init__(self, base_url: str = ""):
        import os as _os
        self.base_url = (base_url or _os.environ.get("MT5_API_URL", "")).rstrip("/")
        self.state = ConnectionState.DISCONNECTED
        self.account_info: Optional[AccountInfo] = None
        self.posiciones_abiertas: List[TradeEvent] = []
        self.ordenes_pendientes: List[TradeEvent] = []
        self.historico: List[TradeEvent] = []
        self._callbacks: Dict[str, List[Callable]] = {}
        self._polling_active = False
        self._poll_thread: Optional[threading.Thread] = None
        self._login: Optional[int] = None
        self._seen: set = set()

    # -- API compatible con WineMT5Connector --
    def connect(self, login: int, password: str = "", server: str = "") -> bool:
        self.state = ConnectionState.CONNECTING
        self._login = login
        try:
            snap = self._accounts_snapshot(login)
            self._apply_snapshot(snap)
            if snap.get("status") != "ok":
                raise RuntimeError(snap.get("error", "worker no listo"))
            self.state = ConnectionState.CONNECTED
            self._fire("connected")
            return True
        except Exception as e:  # noqa: BLE001
            self.state = ConnectionState.ERROR
            self._fire("error", str(e))
            return False

    def disconnect(self):
        self._polling_active = False
        if self._poll_thread:
            self._poll_thread.join(timeout=2)
            self._poll_thread = None
        self.state = ConnectionState.DISCONNECTED
        self._fire("disconnected")

    def refresh_data(self):
        if self._login is None:
            return
        snap = self._accounts_snapshot(self._login)
        new = self._apply_snapshot(snap)
        if new:
            self._fire("event", new)

    def detect_new_events(self) -> List[TradeEvent]:
        before = set(self._seen)
        self.refresh_data()
        return [e for e in self.posiciones_abiertas if e.ticket not in before]

    def start_polling(self, interval: int = 5):
        if self._polling_active:
            return
        self._polling_active = True
        self._poll_thread = threading.Thread(
            target=self._loop, args=(interval,), daemon=True
        )
        self._poll_thread.start()

    def stop_polling(self):
        self._polling_active = False

    def on(self, event: str, cb: Callable):
        self._callbacks.setdefault(event, []).append(cb)

    def get_summary(self) -> Dict:
        a = self.account_info
        if not a:
            return {}
        return {
            "login": a.login, "servidor": a.servidor, "balance": a.balance,
            "equity": a.equity, "margin": a.margin,
            "margin_free": a.margin_free, "margin_level": a.margin_level,
            "profit": a.profit, "leverage": a.leverage,
            "open_positions": len(self.posiciones_abiertas),
            "pending_orders": len(self.ordenes_pendientes),
            "state": a.estado,
        }

    def get_history_summary(self) -> Dict:
        tp = sum(h.profit for h in self.historico)
        return {"total_trades": len(self.historico), "total_profit": tp,
                "net_profit": tp}

    # -- internos --
    def _loop(self, interval: int):
        while self._polling_active:
            try:
                self.refresh_data()
            except Exception:
                pass
            time.sleep(interval)

    def _fire(self, event: str, data=None):
        for cb in self._callbacks.get(event, []):
            try:
                cb(data)
            except Exception:
                pass

    def _accounts_snapshot(self, login: int) -> dict:
        r = requests.get(f"{self.base_url}/accounts", timeout=10)
        r.raise_for_status()
        for row in r.json():
            if row.get("login") == login:
                return row
        raise RuntimeError(f"login {login} no publicado por el backend")

    def _apply_snapshot(self, snap: dict) -> List[TradeEvent]:
        acc = snap.get("account", {})
        self.account_info = AccountInfo(
            login=snap.get("login", 0), nombre=snap.get("name", ""),
            servidor=snap.get("server", ""), compania=acc.get("company", ""),
            saldo=acc.get("balance", 0.0), equity=acc.get("equity", 0.0),
            margin=acc.get("margin", 0.0),
            margin_free=acc.get("margin_free", 0.0),
            margin_level=acc.get("margin_level", 0.0),
            profit=acc.get("profit", 0.0),
            leverage=acc.get("leverage", 0),
            balance=acc.get("balance", 0.0), estado=snap.get("status", ""),
        )
        r = requests.get(
            f"{self.base_url}/positions", params={"login": snap.get("login")},
            timeout=10,
        )
        r.raise_for_status()
        fresh: List[TradeEvent] = []
        for p in r.json():
            t = int(p.get("ticket", 0))
            ev = TradeEvent(
                tipo="TRADE", simbolo=p.get("symbol", ""),
                tipo_operacion=str(p.get("type_name", p.get("type", ""))),
                volumen=float(p.get("volume", 0)),
                precio=float(p.get("price_current", p.get("price_open", 0))),
                stop_loss=float(p.get("sl", 0)),
                take_profit=float(p.get("tp", 0)),
                profit=float(p.get("profit", 0)),
                swap=float(p.get("swap", 0)),
                timestamp=datetime.now(), ticket=t, estado="OPEN",
            )
            if t not in self._seen:
                self._seen.add(t)
                fresh.append(ev)
        self.posiciones_abiertas = fresh
        try:
            rd = requests.get(
                f"{self.base_url}/deals",
                params={"login": snap.get("login"), "days": 30}, timeout=10,
            )
            rd.raise_for_status()
            self.historico = [
                TradeEvent(
                    tipo="HISTORY", simbolo=d.get("symbol", ""),
                    tipo_operacion=str(d.get("type", "")),
                    volumen=float(d.get("volume", 0)),
                    precio=float(d.get("price", 0)),
                    profit=float(d.get("profit", 0)),
                    commission=float(d.get("commission", 0)),
                    swap=float(d.get("swap", 0)),
                    timestamp=datetime.now(),
                    ticket=int(d.get("ticket", 0)),
                    comentario=str(d.get("comment", "")),
                    estado="CLOSED",
                )
                for d in rd.json()
            ]
        except Exception:
            pass
        return fresh


MT5Connector = RestMT5Connector
MT5_AVAILABLE = True
