# Entorno de prácticas del módulo 5071 · Modelos de Inteligencia Artificial
# Sustituye al Dockerfile antiguo, que fijaba python:3.6 (fuera de soporte desde 2021).
FROM python:3.12-slim

# Dependencias del sistema que necesitan algunas ruedas científicas
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home/mia

# Primero las dependencias: si no cambian, esta capa se reutiliza de la caché
COPY requirements-ia.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements-ia.txt

EXPOSE 8888
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", \
     "--allow-root", "--NotebookApp.token=cursoia"]
