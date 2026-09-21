"""
Backend MT5 para Windows - 1 worker (proceso) por terminal.

Por qué: la librería MetaTrader5 solo mantiene UNA conexión IPC activa
por proceso Python. Para N cuentas -> N workers vía multiprocessing,
cada uno con mt5.initialize(path=<su terminal64.exe>).

Uso en Windows:
  1. Edita ACCOUNTS abajo (path portable, login, password investor, server)
  2. pip install -r requirements.txt
  3. python api.py
  4. Abre http://localhost:8000/accounts

Endpoints solo lectura (las passwords investor nunca salen del worker):
  GET /health
  GET /accounts
  GET /positions?login=103515
  GET /deals?login=103515&days=30
"""

import time
import traceback
from datetime import datetime, timedelta
from multiprocessing import Manager, Process
from typing import Dict, List

from fastapi import FastAPI, HTTPException, Query
import uvicorn

# ---------------------------------------------------------------------------
# CONFIGURA AQUÍ TUS CUENTAS (una entrada por terminal portable)
# ---------------------------------------------------------------------------
ACCOUNTS = [
    {
        "login": 103515,
        "password": "mI6$*PGeTQ",   # investor (solo lectura)
        "server": "ThePropTrade-Server",
        "path": r"C:\MT5-Fondeo1\terminal64.exe",
        "name": "Fondeo1",
    },
    {
        "login": 102846,
        "password": "Kk708ad*dq",   # investor (solo lectura)
        "server": "ThePropTrade-Server",
        "path": r"C:\MT5-Fondeo2\terminal64.exe",
        "name": "Fondeo2",
    },
]

POLL_INTERVAL = 5  # segundos


def worker_loop(cfg: dict, store: dict):
    """Proceso dedicado a UN terminal. No compartir mt5 entre procesos."""
    import MetaTrader5 as mt5

    login = cfg["login"]
    key = str(login)
    store[key] = {"status": "starting", "updated_at": None}

    def set_error(msg: str):
        store[key] = {
            "status": "error", "error": msg,
            "updated_at": datetime.now().isoformat(),
            "account": {}, "positions": [], "deals": [],
        }

    try:
        if not mt5.initialize(path=cfg["path"]):
            set_error(f"initialize failed: {mt5.last_error()}")
            return
        ok = mt5.login(login, password=cfg["password"], server=cfg["server"])
        if not ok:
            set_error(f"login failed: {mt5.last_error()}")
            mt5.shutdown()
            return
    except Exception as e:  # noqa: BLE001
        set_error(f"exception init: {e}\n{traceback.format_exc()[-500:]}")
        return

    while True:
        try:
            acc = mt5.account_info()
            if acc is None:
                raise RuntimeError(f"account_info None: {mt5.last_error()}")
            positions = mt5.positions_get() or []
            deals_raw = mt5.history_deals_get(
                datetime.now() - timedelta(days=30), datetime.now()
            ) or []

            store[key] = {
                "status": "ok",
                "updated_at": datetime.now().isoformat(),
                "name": cfg.get("name", str(login)),
                "server": cfg["server"],
                "account": {
                    "login": acc.login, "name": acc.name, "server": acc.server,
                    "company": acc.company, "balance": acc.balance,
                    "equity": acc.equity, "margin": acc.margin,
                    "margin_free": acc.margin_free,
                    "margin_level": acc.margin_level, "profit": acc.profit,
                    "leverage": acc.leverage, "currency": acc.currency,
                },
                "positions": [
                    {
                        "ticket": p.ticket, "symbol": p.symbol,
                        "type": p.type, "type_name": getattr(p, "type_name", str(p.type)),
                        "volume": p.volume, "price_open": p.price_open,
                        "price_current": p.price_current, "sl": p.sl, "tp": p.tp,
                        "profit": p.profit, "swap": p.swap,
                        "time": datetime.fromtimestamp(p.time).isoformat(),
                    }
                    for p in positions
                ],
                "deals": [
                    {
                        "ticket": d.ticket, "order": d.order, "symbol": d.symbol,
                        "type": d.type, "volume": d.volume, "price": d.price,
                        "profit": d.profit, "commission": d.commission,
                        "swap": d.swap, "comment": d.comment,
                        "time": datetime.fromtimestamp(d.time).isoformat(),
                    }
                    for d in deals_raw[-200:]
                ],
            }
        except Exception as e:  # noqa: BLE001 - el worker nunca debe morir
            try:
                set_error(f"poll error: {e}")
            except Exception:
                pass
        time.sleep(POLL_INTERVAL)


app = FastAPI(title="MT5 Read-only Backend")
_manager = Manager()
_store: Dict = _manager.dict()
_workers: List[Process] = []


@app.on_event("startup")
def _startup():
    for cfg in ACCOUNTS:
        p = Process(target=worker_loop, args=(cfg, _store), daemon=True)
        p.start()
        _workers.append(p)


@app.get("/health")
def health():
    return {
        "ok": True,
        "workers": len(_workers),
        "alive": [p.is_alive() for p in _workers],
        "logins": [c["login"] for c in ACCOUNTS],
    }


@app.get("/accounts")
def accounts():
    out = []
    for cfg in ACCOUNTS:
        snap = dict(_store.get(str(cfg["login"]), {}))
        out.append({
            "login": cfg["login"], "name": cfg.get("name", str(cfg["login"])),
            "server": cfg["server"], "status": snap.get("status", "starting"),
            "updated_at": snap.get("updated_at"),
            "error": snap.get("error"),
            "account": snap.get("account", {}),
            "open_positions": len(snap.get("positions", [])),
        })
    return out


def _snapshot(login: int) -> dict:
    snap = _store.get(str(login))
    if not snap:
        raise HTTPException(404, f"login {login} sin worker (¿arrancado?)")
    return dict(snap)


@app.get("/positions")
def positions(login: int = Query(...)):
    snap = _snapshot(login)
    if snap.get("status") != "ok":
        raise HTTPException(502, snap.get("error", "worker no listo"))
    return snap.get("positions", [])


@app.get("/deals")
def deals(login: int = Query(...), days: int = Query(30, le=90)):
    snap = _snapshot(login)
    if snap.get("status") != "ok":
        raise HTTPException(502, snap.get("error", "worker no listo"))
    all_deals = snap.get("deals", [])
    if not days:
        return all_deals
    cutoff = datetime.now() - timedelta(days=days)
    return [d for d in all_deals if d.get("time", "") >= cutoff.isoformat()]


if __name__ == "__main__":
    # Importante: multiprocessing en Windows necesita el guard main.
    uvicorn.run(app, host="0.0.0.0", port=8000)
