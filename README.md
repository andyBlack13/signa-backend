# Signa Backend

Este es el backend de la aplicación **Signa**. Está desarrollado en Python usando Flask (o el framework que uses).

## Instalación

1. Clona el repositorio:

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd signa-backend

2. Crea y activa el entorno virtual:

    ```bash
    python -m venv env  # Solo la primera vez
    .\env\Scripts\activate  # En Windows
    # o
    source env/bin/activate  # En Linux/macOS

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt

4. Ejecuta la aplicación:

    ```bash
    uvicorn main:app --reload


Este comando iniciará el servidor de FastAPI en el puerto 8000 (por defecto), y podrán acceder a tu API en http://localhost:8000.