"""
Sistema de notificaciones para eventos de trading.
Soporta: notify-send (Linux nativo), plyer, sistema nativo (Windows), macOS, terminal.
"""

import os
import sys
import platform
import subprocess
import warnings
from datetime import datetime
from typing import Optional
from enum import Enum

try:
    import plyer
    from plyer import notification
    PLYER_AVAILABLE = True
except ImportError:
    PLYER_AVAILABLE = False

try:
    import dbus
    DBUS_AVAILABLE = True
except ImportError:
    DBUS_AVAILABLE = False


class NotifLevel(Enum):
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    ALERT = "alert"


class TradeNotifier:
    """Notificador de eventos de trading."""

    def __init__(self, title_prefix: str = "MT5 Monitor"):
        self.title_prefix = title_prefix
        self.platform_name = platform.system()
        self._notify_send_available = self._check_notify_send()

    def _check_notify_send(self) -> bool:
        """Verificar si notify-send está disponible (Linux)."""
        if self.platform_name != "Linux":
            return False
        try:
            result = subprocess.run(
                ["which", "notify-send"],
                capture_output=True, timeout=2
            )
            return result.returncode == 0
        except Exception:
            return False

    def notify(self, level: NotifLevel, title: str, message: str, timeout: int = 10):
        """Enviar notificación usando el mejor método disponible."""
        full_title = f"[{self.title_prefix}] {title}"
        try:
            if self.platform_name == "Linux" and self._notify_send_available:
                self._notify_send(full_title, message, level, timeout)
            elif PLYER_AVAILABLE and self._plyer_available():
                self._plyer_notify(full_title, message, level, timeout)
            else:
                self._terminal_notify(level, full_title, message)
        except Exception:
            self._terminal_notify(level, full_title, message)

    def _plyer_available(self) -> bool:
        """Verificar si plyer funciona correctamente."""
        if not PLYER_AVAILABLE:
            return False
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                # Test if plyer can actually send a notification
                return True
        except Exception:
            return False

    def _notify_send(self, title: str, message: str, level: NotifLevel, timeout: int):
        """Usar notify-send nativo de Linux."""
        icon = self._get_notify_icon(level)
        try:
            cmd = [
                "notify-send",
                "-u", self._get_urgency(level),
                "-t", str(timeout * 1000),
                "-i", icon,
                title,
                message
            ]
            subprocess.run(cmd, capture_output=True, timeout=5)
        except Exception:
            self._terminal_notify(level, title, message)

    def _plyer_notify(self, title: str, message: str, level: NotifLevel, timeout: int):
        """Usar plyer con manejo de errores."""
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", UserWarning)
                icon = self._get_plyer_icon(level)
                notification.notify(
                    title=title,
                    message=message,
                    app_name=self.title_prefix,
                    timeout=timeout,
                    app_icon=icon
                )
        except Exception:
            self._terminal_notify(level, title, message)

    def _terminal_notify(self, level: NotifLevel, title: str, message: str):
        """Notificación por terminal con colores."""
        color_map = {
            NotifLevel.INFO: "\033[94m",
            NotifLevel.SUCCESS: "\033[92m",
            NotifLevel.WARNING: "\033[93m",
            NotifLevel.ALERT: "\033[91m",
        }
        reset = "\033[0m"
        symbol = {"INFO": "ℹ", "SUCCESS": "✓", "WARNING": "⚠", "ALERT": "✗"}
        color = color_map.get(level, "")
        print(f"{color}[{symbol.get(level.value.upper()[:1], '?')}] {title}: {message}{reset}")

    def _get_notify_icon(self, level: NotifLevel) -> str:
        """Obtener icono para notify-send."""
        icon_map = {
            NotifLevel.INFO: "dialog-information",
            NotifLevel.SUCCESS: "dialog-ok",
            NotifLevel.WARNING: "dialog-warning",
            NotifLevel.ALERT: "dialog-error"
        }
        return icon_map.get(level, "dialog-information")

    def _get_plyer_icon(self, level: NotifLevel) -> str:
        """Obtener icono para plyer."""
        icon_map = {
            NotifLevel.INFO: "dialog-information",
            NotifLevel.SUCCESS: "dialog-ok",
            NotifLevel.WARNING: "dialog-warning",
            NotifLevel.ALERT: "dialog-error"
        }
        return icon_map.get(level, "dialog-information")

    def _get_urgency(self, level: NotifLevel) -> str:
        """Obtener urgencia para notify-send."""
        urgency_map = {
            NotifLevel.INFO: "low",
            NotifLevel.SUCCESS: "normal",
            NotifLevel.WARNING: "critical",
            NotifLevel.ALERT: "critical"
        }
        return urgency_map.get(level, "low")

    def on_new_position(self, position: dict):
        """Notificar apertura de nueva posición."""
        self.notify(
            NotifLevel.SUCCESS,
            "Nueva Posición",
            f"{position['tipo']} {position['simbolo']} {position['volumen']} lots @ {position['precio']}"
        )

    def on_close_position(self, position: dict, profit: float):
        """Notificar cierre de posición."""
        level = NotifLevel.SUCCESS if profit >= 0 else NotifLevel.ALERT
        emoji = "🟢" if profit >= 0 else "🔴"
        self.notify(
            level,
            f"{emoji} Posición Cerrada",
            f"{position['simbolo']}: P&L = ${profit:.2f} | Ticket #{position['ticket']}"
        )

    def on_new_order(self, order: dict):
        """Notificar nueva orden pendiente."""
        self.notify(
            NotifLevel.INFO,
            "Nueva Orden Pendiente",
            f"{order['tipo_operacion']} {order['simbolo']} @ {order['precio']} | SL: {order['stop_loss']}"
        )

    def on_account_update(self, summary: dict):
        """Notificar actualización de cuenta."""
        self.notify(
            NotifLevel.INFO,
            "Cuenta Actualizada",
            f"Balance: ${summary['balance']:.2f} | Equity: ${summary['equity']:.2f} | P&L: ${summary['profit']:.2f}"
        )

    def on_connection_change(self, status: str):
        """Notificar cambio de estado de conexión."""
        if status == "connected":
            self.notify(NotifLevel.SUCCESS, "Conectado", "Conexión a MT5 establecida")
        elif status == "disconnected":
            self.notify(NotifLevel.WARNING, "Desconectado", "Conexión a MT5 cerrada")
        elif status == "error":
            self.notify(NotifLevel.ALERT, "Error", "Error en la conexión MT5")
