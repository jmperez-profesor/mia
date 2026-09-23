# MT5 Viewer — Monitor de Cuentas de Fondeo

Aplicación gráfica para visualizar y monitorizar cuentas de trading en MetaTrader 5 a través de Wine/Bottles, con modo investor (lectura).

## Características

- 📊 **Dashboard visual** con tarjetas de cuenta (balance, equity, margen, P&L)
- 📈 **Posiciones abiertas** en tiempo real
- 📋 **Órdenes pendientes** visualizadas
- 📜 **Historial de operaciones** con filtros
- 🔔 **Notificaciones** automáticas al abrir/cerrar posiciones
- 🔄 **Polling automático** para detección de eventos
- 💾 **Persistencia** de cuentas guardadas (JSON local)
- 🍺 **Conexión real** con MT5 a través de Bottles/Wine
- 📝 **Logs** de actividad

## Requisitos

- MT5 instalado en **Bottles** (nombre de bottle: `MT5-FTMO-Challenge`)
- Python 3.11+
- `plyer` para notificaciones
- `notify-send` disponible en Linux

## Instalación

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

> **Nota:** El paquete `MetaTrader5` de PyPI es solo para Windows. Esta app conecta directamente con MT5 instalado en Bottles/Wine a través del sistema de archivos del Wine prefix.

## Uso

```bash
python3 app.py
```

1. Haz clic en **"+ Añadir Cuenta"** para configurar una cuenta MT5
2. Introduce el **login, contraseña investor y servidor**
3. Pulsa **"Conectar"** para conectar (modo lectura/investor)
4. Pulsa **"▶ Monitor"** para activar la detección de eventos
5. Recibirás notificaciones cuando se abran/cierren operaciones

## Estructura de archivos

```
mt5_viewer/
├── app.py              # Aplicación principal (tkinter GUI)
├── wine_mt5.py         # Conector MT5 real a través de Wine/Bottles
├── mt5_connector.py    # Capa de compatibilidad con MT5Connector
├── notifier.py         # Sistema de notificaciones (notify-send)
├── config.py           # Gestión de configuración y cuentas
├── requirements.txt    # Dependencias Python
├── run.sh             # Script de lanzamiento
└── README.md          # Este archivo
```

## Cómo funciona

La app lee los archivos de **logs de MT5** ubicados en:
```
~/.var/app/com.usebottles.bottles/data/bottles/bottles/MT5-FTMO-Challenge/drive_c/Program Files/MetaTrader 5/logs/
```

Los logs de MT5 contienen eventos de trading codificados (formato binario UTF-16 LE) que el módulo `wine_mt5.py` parsea para detectar:

- 🟢 **Nueva posición abierta** (orden de mercado ejecutada)
- 🔴 **Posición cerrada** (deal completado)
- ⚠️ **Modificación de SL/TP**
- 📢 **Cambio de estado de conexión**

## Datos de configuración

Las cuentas se guardan en `~/.mt5_viewer/accounts.json` (contraseñas en texto plano, usa con precaución).

## Seguridad

- Usa siempre contraseñas de **tipo investor** (solo lectura)
- Las credenciales se almacenan localmente en formato JSON
- No compartas el archivo de configuración

## Notificaciones

La app usa `notify-send` nativo de Linux para notificaciones de escritorio. Cuando se detectan:

- 🟢 **Nueva posición abierta** → Notificación de éxito
- 🔴 **Posición cerrada** → Notificación de alerta (roja si pérdida)
- 📢 **Cambio de estado de conexión** → Notificación informativa

## Licencia

CC BY-NC-SA 4.0
