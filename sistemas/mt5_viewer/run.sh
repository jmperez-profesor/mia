#!/bin/bash
# Lanzador MT5 Viewer

cd "$(dirname "$0")"

# Crear venv si no existe
if [ ! -d "venv" ]; then
    echo "Creando entorno virtual..."
    python3 -m venv venv
fi

source venv/bin/activate

# Instalar dependencias si es necesario
pip install -r requirements.txt 2>/dev/null

echo "Iniciando MT5 Viewer..."
python3 app.py
