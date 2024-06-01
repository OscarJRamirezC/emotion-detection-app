# Emotion Detection App

## Configuración y Ejecución

### API con FastAPI

1. Crear un entorno virtual e instalar dependencias:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    pip install -r api/requirements.txt
    ```

2. Ejecutar el servidor FastAPI:
    ```bash
    uvicorn api.main:app --reload
    ```

### Aplicación Web

1. Crear un entorno virtual e instalar dependencias:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    pip install -r webapp/requirements.txt
    ```

2. Ejecutar el servidor Flask:
    ```bash
    python webapp/app.py
    ```

### Integración y Pruebas

- Accede a `http://localhost:5000` en tu navegador.
- Sube una imagen y revisa los resultados de la predicción.

### Estructura del Proyecto

