"""
Gestor de configuración y persistencia de cuentas MT5.
Almacena cuentas en un archivo JSON local.
"""

import json
import os
from pathlib import Path
from typing import List, Optional, Dict
from dataclasses import dataclass, field, asdict
from datetime import datetime

CONFIG_DIR = Path.home() / ".mt5_viewer"
CONFIG_FILE = CONFIG_DIR / "config.json"
ACCOUNTS_FILE = CONFIG_DIR / "accounts.json"


@dataclass
class SavedAccount:
    nombre: str
    login: int
    password: str
    servidor: str
    color: str = "#00ff88"
    created_at: str = ""

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()


class ConfigManager:
    """Gestiona la configuración y cuentas guardadas."""

    def __init__(self):
        CONFIG_DIR.mkdir(exist_ok=True)
        self.accounts: List[SavedAccount] = self._load_accounts()

    def _load_accounts(self) -> List[SavedAccount]:
        """Cargar cuentas desde archivo."""
        if not ACCOUNTS_FILE.exists():
            return []
        try:
            with open(ACCOUNTS_FILE) as f:
                data = json.load(f)
                return [SavedAccount(**a) for a in data]
        except (json.JSONDecodeError, KeyError):
            return []

    def _save_accounts(self):
        """Guardar cuentas en archivo."""
        with open(ACCOUNTS_FILE, "w") as f:
            json.dump([asdict(a) for a in self.accounts], f, indent=2)

    def add_account(self, nombre: str, login: int, password: str, servidor: str, color: str = "#00ff88") -> SavedAccount:
        """Añadir una nueva cuenta."""
        account = SavedAccount(
            nombre=nombre, login=login, password=password,
            servidor=servidor, color=color
        )
        self.accounts.append(account)
        self._save_accounts()
        return account

    def remove_account(self, index: int):
        """Eliminar cuenta por índice."""
        if 0 <= index < len(self.accounts):
            self.accounts.pop(index)
            self._save_accounts()

    def update_account(self, index: int, nombre: str, login: int, password: str, servidor: str, color: str) -> bool:
        """Actualizar datos de una cuenta."""
        if 0 <= index < len(self.accounts):
            self.accounts[index] = SavedAccount(
                nombre=nombre, login=login, password=password,
                servidor=servidor, color=color,
                created_at=self.accounts[index].created_at
            )
            self._save_accounts()
            return True
        return False

    def find_account_by_login(self, login: int) -> Optional[int]:
        """Buscar índice de cuenta por login."""
        for i, acc in enumerate(self.accounts):
            if acc.login == login:
                return i
        return None

    def get_account(self, index: int) -> Optional[SavedAccount]:
        """Obtener cuenta por índice."""
        if 0 <= index < len(self.accounts):
            return self.accounts[index]
        return None

    def get_all_accounts(self) -> List[SavedAccount]:
        """Obtener todas las cuentas."""
        return self.accounts

    def get_colors(self) -> List[str]:
        """Paleta de colores para cuentas."""
        return [
            "#00ff88", "#ff6b6b", "#4ecdc4", "#45b7d1",
            "#f9ca24", "#6c5ce7", "#fd79a8", "#00b894",
            "#e17055", "#0984e3", "#fdcb6e", "#e84393"
        ]

    def update_connection_status(self, index: int, status: str, login: int, equity: float, balance: float, profit: float):
        """Actualizar estado de conexión de una cuenta."""
        if 0 <= index < len(self.accounts):
            # El estado se almacena internamente; para persistencia extendida
            pass


class LogManager:
    """Gestor de logs de eventos."""

    def __init__(self):
        self.log_dir = CONFIG_DIR / "logs"
        self.log_dir.mkdir(exist_ok=True)
        self.current_log: List[Dict] = []

    def add_entry(self, event_type: str, message: str, details: Dict = None):
        """Añadir entrada al log."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "event_type": event_type,
            "message": message,
            "details": details or {}
        }
        self.current_log.append(entry)
        self._save_log()

    def _save_log(self):
        """Guardar log en archivo."""
        log_file = self.log_dir / f"session_{datetime.now().strftime('%Y%m%d')}.json"
        try:
            with open(log_file, "w") as f:
                json.dump(self.current_log[-1000:], f, indent=2)
        except Exception:
            pass

    def get_recent_events(self, limit: int = 50) -> List[Dict]:
        """Obtener eventos recientes."""
        return self.current_log[-limit:]
