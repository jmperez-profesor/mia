# Backend MT5 en Windows (portable, modo lectura)

Este backend corre **en el Windows donde están los terminales**.
El dashboard (Linux o Windows) lo consume por HTTP, sin IPC.

## 1. Terminales (ya hecho)

- `C:\MT5-Fondeo1\terminal64.exe` con acceso directo que lleva `--portable` (o flag `/portable`)
- `C:\MT5-Fondeo2\terminal64.exe` igual
- Cada terminal logueado con su cuenta usando **contraseña de inversor** y dejado corriendo.
- En MT5: Herramientas > Opciones > Asesores Expertos > permitir trading algorítmico
  (solo lectura vía Python, no abre operaciones si usas investor).

## 2. Backend

```powershell
cd C:\mt5-backend
pip install -r requirements.txt
# edita ACCOUNTS en api.py (login, password investor, server, path)
python api.py
```

Verifica:

- http://localhost:8000/health
- http://localhost:8000/accounts

Si el dashboard está en otra máquina (tu Ubuntu), abre el puerto 8000
en el firewall de Windows solo para tu IP, o usa VPN/Tailscale.
Recomendado: no exponer 8000 a internet. Para 24/7 usa VPS Windows.

## 3. Dashboard

En el dashboard pon `MT5_API_URL=http://IP_DEL_WINDOWS:8000` y usa
`rest_connector.py` (misma interfaz que el conector Wine).
