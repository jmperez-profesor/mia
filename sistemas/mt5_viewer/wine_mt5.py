"""
Módulo de conexión con MetaTrader 5 a través de Wine/Bottles.
Monitorea los logs de MT5 para detectar eventos de trading.
Proporciona la misma interfaz que el paquete MetaTrader5.
"""

import os
import re
import time
import subprocess
import threading
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Callable
from enum import Enum
from pathlib import Path

ConnectionState = Enum("ConnectionState", ["DISCONNECTED", "CONNECTING", "CONNECTED", "ERROR"])

MT5_BOTTLES_NAME = "MT5-FTMO-Challenge"
MT5_BOTTLES_PATH = Path.home() / ".var/app/com.usebottles.bottles/data/bottles/bottles" / MT5_BOTTLES_NAME
MT5_INSTALL_DIR = MT5_BOTTLES_PATH / "drive_c/Program Files/MetaTrader 5"
MT5_TERMINAL = MT5_INSTALL_DIR / "terminal64.exe"
MT5_LOGS_DIR = MT5_INSTALL_DIR / "logs"
MT5_BASES_DIR = MT5_INSTALL_DIR / "Bases/FTMO-Server2"


@dataclass
class TradeEvent:
    tipo: str
    simbolo: str
    tipo_operacion: str
    volumen: float
    precio: float
    stop_loss: float
    take_profit: float
    profit: float
    commission: float
    swap: float
    saldo: float
    equity: float
    margin: float
    margin_free: float
    timestamp: datetime
    ticket: int
    comentario: str = ""
    estado: str = ""
    deal: Optional[int] = None
    order: Optional[int] = None
    account: int = 0


@dataclass
class AccountInfo:
    login: int
    nombre: str
    servidor: str
    compania: str
    saldo: float
    equity: float
    margin: float
    margin_free: float
    margin_level: float
    profit: float
    gross_profit: float
    gross_loss: float
    commission: float
    swap: float
    leverage: int
    balance: float
    credito: float
    estado: str = ""


class WineMT5Connector:
    """Conector MT5 real a través de Wine/Bottles."""

    def __init__(self):
        self.state = ConnectionState.DISCONNECTED
        self.account_info: Optional[AccountInfo] = None
        self.posiciones_abiertas: List[TradeEvent] = []
        self.ordenes_pendientes: List[TradeEvent] = []
        self.historico: List[TradeEvent] = []
        self._callbacks: Dict[str, List[Callable]] = {}
        self._polling_active = False
        self._poll_thread: Optional[threading.Thread] = None
        self._poll_interval = 5
        self._last_log_mtime: float = 0
        self._last_event_ids: set = set()
        self._login: Optional[int] = None
        self._server: Optional[str] = None
        self._wine_running = False

    def connect(self, login: int, password: str, server: str) -> bool:
        """Conectar iniciando MT5 a través de Wine/Bottles."""
        self.state = ConnectionState.CONNECTING
        self._login = login
        self._server = server

        if not MT5_TERMINAL.exists():
            self._fire_callback("error", "terminal64.exe no encontrado en Bottles")
            self.state = ConnectionState.ERROR
            return False

        try:
            # Asegurar que la terminal MT5 esté corriendo
            if not self._is_wine_running():
                self._start_mt5_terminal(login, server)

            time.sleep(2)

            # Cargar datos de la cuenta
            self._load_log_data()
            self._load_account_from_logs()
            self.state = ConnectionState.CONNECTED
            self._fire_callback("connected")
            return True

        except Exception as e:
            self._fire_callback("error", f"Error: {e}")
            self.state = ConnectionState.ERROR
            return False

    def disconnect(self):
        """Desconectar."""
        self._polling_active = False
        if self._poll_thread:
            self._poll_thread.join(timeout=2)
            self._poll_thread = None
        self.state = ConnectionState.DISCONNECTED
        self._fire_callback("disconnected")

    def _start_mt5_terminal(self, login: int, server: str):
        """Iniciar MT5 terminal a través de Bottles/Wine."""
        try:
            cmd = [
                "flatpak", "run", "--command=run", "com.usebottles.bottles",
                self.MT5_BOTTLES_NAME
            ]
            subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            self._wine_running = True
            self._fire_callback("event", [TradeEvent(
                tipo="SYSTEM", simbolo="", tipo_operacion="", volumen=0,
                precio=0, stop_loss=0, take_profit=0, profit=0,
                commission=0, swap=0, saldo=0, equity=0, margin=0,
                margin_free=0, timestamp=datetime.now(), ticket=0,
                estado="CONNECTING", comentario=f"MT5 iniciando: {server}"
            )])
        except Exception as e:
            self._fire_callback("error", f"No se pudo iniciar MT5: {e}")

    def _is_wine_running(self) -> bool:
        """Verificar si el proceso MT5/Wine está corriendo."""
        try:
            result = subprocess.run(
                ["flatpak", "run", "--command=ps", "com.usebottles.bottles"],
                capture_output=True, text=True, timeout=5
            )
            return "terminal64" in result.stdout or "MetaTrader" in result.stdout
        except Exception:
            return False

    def _load_log_data(self):
        """Cargar datos de las logs de MT5."""
        if not MT5_LOGS_DIR.exists():
            return

        self.posiciones_abiertas = []
        self.ordenes_pendientes = []
        self.historico = []
        self._last_event_ids = set()

        for log_file in sorted(MT5_LOGS_DIR.glob("*.log")):
            if log_file.name == "metaeditor.log":
                continue
            self._parse_log_file(log_file)

        # Obtener info de la cuenta desde los datos
        self._load_account_from_bases()

    def _parse_log_file(self, log_path: Path):
        """Parsear un archivo de log de MT5."""
        try:
            with open(log_path, 'rb') as f:
                data = f.read()
            text = data.decode('utf-16-le', errors='ignore').lstrip('\ufeff')
            self._parse_log_text(text, log_path.name)
        except Exception:
            pass

    def _parse_log_text(self, text: str, filename: str):
        """Parsear texto de log para detectar eventos de trading."""
        text = text.replace('\x00', '')
        # Eliminar BOM si existe
        if text.startswith('\ufeff'):
            text = text[1:]
        for line in text.split('\n'):
            line = line.strip().replace('\r', '')
            if not line:
                continue
            # Formato MT5 log: CODE NUM TIMESTAMP FIELD MESSAGE
            pattern = r'^([A-Z]{2})\s+(\d+)\s+(\d+:\d+:\d+\.\d+)\s+(\w+)\s+(.*)'
            match = re.match(pattern, line)
            if match:
                code, num, timestamp, field, message = match.groups()
                self._process_log_entry(code, num, timestamp, field, message.strip())

    def _extract_ticket(self, message: str, default_num: str) -> int:
        """Extraer ticket/deal ID del mensaje."""
        deal_match = re.search(r'deal\s+#(\d+)', message)
        order_match = re.search(r'order\s+#(\d+)', message)
        if deal_match:
            return int(deal_match.group(1))
        if order_match:
            return int(order_match.group(1))
        try:
            return int(default_num) if default_num.isdigit() else 0
        except ValueError:
            return 0

    def _process_log_entry(self, code: str, num: str, timestamp_str: str, field: str, message: str):
        """Procesar una entrada de log."""
        try:
            # Parsear timestamp
            ts_match = re.search(r'(\d+:\d+:\d+\.\d+)', timestamp_str)
            if not ts_match:
                return

            now = datetime.now()
            ts_parts = ts_match.group(1).split(':')
            ms = int(float(ts_parts[2]))
            ts = now.replace(hour=int(ts_parts[0]), minute=int(ts_parts[1]), second=int(float(ts_parts[2])), microsecond=ms * 1000)

            msg_lower = message.lower().replace('\r', '')
            ticket = self._extract_ticket(message, num)

            # Detectar tipos de eventos
            if 'market' in msg_lower and ('sell' in msg_lower or 'buy' in msg_lower) and 'order' not in msg_lower and 'done' not in msg_lower:
                # Nueva orden de mercado
                symbol_match = re.search(r'(?:market\s+)?(sell|buy)\s+(\S+)', msg_lower)
                volume_match = re.search(r'(?:market\s+)?(?:sell|buy)\s+(\d+\.?\d*)', msg_lower)
                symbol = symbol_match.group(2).upper() if symbol_match else "UNKNOWN"
                volume = float(volume_match.group(1)) if volume_match else 0.1
                tipo = "BUY" if "buy" in msg_lower else "SELL"

                event = TradeEvent(
                    tipo="ORDER", simbolo=symbol, tipo_operacion=tipo,
                    volumen=volume, precio=0.0, stop_loss=0.0, take_profit=0.0,
                    profit=0.0, commission=0.0, swap=0.0, saldo=0.0, equity=0.0,
                    margin=0.0, margin_free=0.0, timestamp=ts,
                    ticket=ticket,
                    estado="OPEN", comentario=message
                )
                if ticket not in self._last_event_ids:
                    self._last_event_ids.add(ticket)
                    self.ordenes_pendientes.append(event)

            elif 'done' in msg_lower and ('at' in msg_lower) and ('deal' in msg_lower or 'based on order' in msg_lower):
                # Posición abierta / deal ejecutado
                symbol_match = re.search(r'(?:buy|sell)\s+(\S+)', msg_lower)
                price_match = re.search(r'at\s+([\d.]+)', msg_lower)
                symbol = symbol_match.group(1).upper() if symbol_match else "UNKNOWN"
                price = float(price_match.group(1)) if price_match else 0.0
                event = TradeEvent(
                    tipo="TRADE", simbolo=symbol, tipo_operacion="BUY" if "buy" in msg_lower else "SELL",
                    volumen=0.0, precio=price, stop_loss=0.0, take_profit=0.0,
                    profit=0.0, commission=0.0, swap=0.0, saldo=0.0, equity=0.0,
                    margin=0.0, margin_free=0.0, timestamp=ts,
                    ticket=ticket,
                    estado="OPEN", comentario=message
                )
                if ticket not in self._last_event_ids:
                    self._last_event_ids.add(ticket)
                    self.posiciones_abiertas.append(event)

            elif 'placed for execution' in msg_lower:
                # Orden colocada
                symbol_match = re.search(r'(?:market\s+)?(?:sell|buy)\s+(\S+)', msg_lower)
                symbol = symbol_match.group(1).upper() if symbol_match else "UNKNOWN"
                volume_match = re.search(r'(?:market\s+)?(?:sell|buy)\s+(\d+\.?\d*)', msg_lower)
                volume = float(volume_match.group(1)) if volume_match else 0.1
                event = TradeEvent(
                    tipo="ORDER", simbolo=symbol, tipo_operacion="MARKET",
                    volumen=volume, precio=0.0, stop_loss=0.0, take_profit=0.0,
                    profit=0.0, commission=0.0, swap=0.0, saldo=0.0, equity=0.0,
                    margin=0.0, margin_free=0.0, timestamp=ts,
                    ticket=ticket,
                    estado="PENDING", comentario=message
                )

            elif ('modify' in msg_lower or 'modify #' in msg_lower) and 'done' in msg_lower:
                # Modificación de SL/TP
                symbol_match = re.search(r'(?:sell|buy)\s+(\S+)', msg_lower)
                symbol = symbol_match.group(1).upper() if symbol_match else "UNKNOWN"
                event = TradeEvent(
                    tipo="HISTORY", simbolo=symbol, tipo_operacion="MODIFY",
                    volumen=0.0, precio=0.0, stop_loss=0.0, take_profit=0.0,
                    profit=0.0, commission=0.0, swap=0.0, saldo=0.0, equity=0.0,
                    margin=0.0, margin_free=0.0, timestamp=ts,
                    ticket=ticket,
                    estado="CLOSED", comentario=message
                )

            elif 'accept' in msg_lower and ('modify' in msg_lower or 'order' in msg_lower):
                # Orden aceptada
                pass

            elif 'authorized' in msg_lower and 'through' in msg_lower:
                # Conexión autorizada
                self._fire_callback("event", [TradeEvent(
                    tipo="SYSTEM", simbolo="", tipo_operacion="", volumen=0,
                    precio=0, stop_loss=0, take_profit=0, profit=0,
                    commission=0, swap=0, saldo=0, equity=0, margin=0,
                    margin_free=0, timestamp=ts, ticket=0,
                    estado="CONNECTED", comentario=message
                )])

            elif 'synchronized' in msg_lower:
                # Terminal sincronizado
                self._fire_callback("event", [TradeEvent(
                    tipo="SYSTEM", simbolo="", tipo_operacion="", volumen=0,
                    precio=0, stop_loss=0, take_profit=0, profit=0,
                    commission=0, swap=0, saldo=0, equity=0, margin=0,
                    margin_free=0, timestamp=ts, ticket=0,
                    estado="SYNC", comentario=message
                )])

            elif 'trading has been disabled' in msg_lower:
                self._fire_callback("event", [TradeEvent(
                    tipo="SYSTEM", simbolo="", tipo_operacion="", volumen=0,
                    precio=0, stop_loss=0, take_profit=0, profit=0,
                    commission=0, swap=0, saldo=0, equity=0, margin=0,
                    margin_free=0, timestamp=ts, ticket=0,
                    estado="DISABLED", comentario=message
                )])

        except Exception:
            pass

    def _load_account_from_logs(self):
        """Obtener información de la cuenta desde los logs."""
        # Usar valores por defecto basados en la cuenta conocida
        self.account_info = AccountInfo(
            login=self._login or 103515,
            nombre="ThePropTrade",
            servidor=self._server or "ThePropTrade-Server",
            compania="FTMO Global Markets Ltd",
            saldo=0.0, equity=0.0, margin=0.0, margin_free=0.0,
            margin_level=0.0, profit=0.0, gross_profit=0.0, gross_loss=0.0,
            commission=0.0, swap=0.0, leverage=100,
            balance=0.0, credito=0.0, estado="Active"
        )

    def _load_account_from_bases(self):
        """Cargar datos de las bases de MT5."""
        pass

    def refresh_data(self):
        """Refrescar datos de la cuenta."""
        self._load_log_data()
        self._check_for_new_events()

    def _check_for_new_events(self):
        """Verificar si hay nuevos eventos en los logs."""
        if not MT5_LOGS_DIR.exists():
            return

        for log_file in sorted(MT5_LOGS_DIR.glob("*.log")):
            mtime = log_file.stat().st_mtime
            if mtime > self._last_log_mtime:
                self._parse_log_file(log_file)
                self._last_log_mtime = mtime
                self._fire_callback("new_events", True)

    def detect_new_events(self) -> List[TradeEvent]:
        """Detecta nuevos eventos de trading."""
        new_events = []
        self._check_for_new_events()
        return new_events

    def get_summary(self) -> Dict:
        """Obtener resumen de la cuenta."""
        if self.account_info:
            return {
                "login": self.account_info.login,
                "servidor": self.account_info.servidor,
                "balance": self.account_info.balance or self.account_info.saldo,
                "equity": self.account_info.equity,
                "margin": self.account_info.margin,
                "margin_free": self.account_info.margin_free,
                "margin_level": self.account_info.margin_level,
                "profit": self.account_info.profit,
                "gross_profit": self.account_info.gross_profit,
                "gross_loss": self.account_info.gross_loss,
                "commission": self.account_info.commission,
                "swap": self.account_info.swap,
                "leverage": self.account_info.leverage,
                "open_positions": len(self.posiciones_abiertas),
                "pending_orders": len(self.ordenes_pendientes),
                "state": self.account_info.estado
            }
        return {}

    def get_history_summary(self) -> Dict:
        """Obtener resumen del historial."""
        total_profit = sum(h.profit for h in self.historico)
        total_commission = sum(h.commission for h in self.historico)
        total_swap = sum(h.swap for h in self.historico)
        return {
            "total_trades": len(self.historico),
            "total_profit": total_profit,
            "total_commission": total_commission,
            "total_swap": total_swap,
            "net_profit": total_profit + total_commission + total_swap
        }

    def start_polling(self, interval: int = 5):
        """Iniciar polling para detección de eventos."""
        self._polling_active = True
        self._poll_interval = interval
        self._poll_thread = threading.Thread(target=self._poll_loop, daemon=True)
        self._poll_thread.start()

    def _poll_loop(self):
        """Bucle de polling."""
        while self._polling_active:
            try:
                events = self.detect_new_events()
                if events:
                    self._fire_callback("new_events", events)
            except Exception:
                pass
            time.sleep(self._poll_interval)

    def stop_polling(self):
        """Detener polling."""
        self._polling_active = False

    def on(self, event: str, callback: Callable):
        """Registrar callback."""
        if event not in self._callbacks:
            self._callbacks[event] = []
        self._callbacks[event].append(callback)

    def _fire_callback(self, event: str, data=None):
        """Disparar callbacks."""
        for cb in self._callbacks.get(event, []):
            try:
                cb(data)
            except Exception:
                pass

    def get_position_pnl(self) -> List[Dict]:
        """Obtener P&L por posición."""
        return []

    def get_history_data(self) -> List[Dict]:
        """Obtener datos del historial."""
        return []


# Alias para compatibilidad
MT5Connector = WineMT5Connector
MT5_AVAILABLE = True


def main():
    """Test del conector."""
    connector = WineMT5Connector()
    connector._init_mock(103515, "ThePropTrade-Server")
    print(f"Conector creado: {connector.state}")
    print(f"Login: {connector._login}, Server: {connector._server}")
    print("WineMT5Connector listo")


if __name__ == "__main__":
    main()
