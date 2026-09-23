"""
Selector de conector MT5.

- Si MT5_API_URL está definida -> backend Windows por HTTP (recomendado,
  N cuentas con N workers en el Windows).
- Si no -> conector Wine/Bottles por logs locales (solo Linux con Bottles).

Ejemplo:
  MT5_API_URL=http://192.168.1.50:8000 python3 app.py
"""

import os

_API_URL = os.environ.get("MT5_API_URL", "").strip()

if _API_URL:
    from rest_connector import (  # noqa: F401
        RestMT5Connector as MT5Connector,
        ConnectionState,
        AccountInfo,
        TradeEvent,
        MT5_AVAILABLE,
    )

    BACKEND_MODE = "rest"
    BACKEND_URL = _API_URL
else:
    from wine_mt5 import (  # noqa: F401
        WineMT5Connector as MT5Connector,
        ConnectionState,
        AccountInfo,
        TradeEvent,
        MT5_AVAILABLE,
    )

    BACKEND_MODE = "wine"
    BACKEND_URL = ""
