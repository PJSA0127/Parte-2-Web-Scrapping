# Web Scraping con Asincronismo, Base de Datos y NLP

## Descripción
Este proyecto es una versión avanzada de web scraping sobre la página: https://quotes.toscrape.com/.  
Se ha rediseñado por completo para dejar de ser un script secuencial simple, convirtiéndose en una aplicación web interactiva de arquitectura Full-Stack.

## Novedades Arquitectónicas
- **Scraping Asíncrono**: Uso de `aiohttp` y `asyncio` para obtener todas las páginas concurrentemente, minimizando el tiempo de ejecución.
- **Base de Datos Relacional**: Implementación de `SQLite` nativo configurado con un ORM (`SQLAlchemy`) con tablas independientes para "Citas", "Autores" y "Tags" en una relación "muchos a muchos".
- **Inteligencia (NLP)**: Uso de `TextBlob` para procesar y puntuar automáticamente el sentimiento (Positivo, Negativo, Neutral) de cada cita obtenida.
- **Dashboard Web UI**: Un frontend diseñado con HTML, **Vanilla CSS** moderno (glassmorphism flexbox / dark mode) y JS interconectado al API que despliega gráficas enriquecidas con `Chart.js`.
- **Backend Moderno**: API servida mediante `FastAPI` que orquesta la ejecución y distribución de datos sin bloquear operaciones mediante endpoints concurrentes.

## Tecnologías principales utilizadas
- Python (FastAPI, aiohttp, SQLAlchemy, TextBlob)
- UI: HTML5, CSS3, jQuery, Chart.js

## Ejecución del proyecto

1. **Instalar dependencias**:
```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

2. **Levantar el Servicio Web**:
```bash
uvicorn main:app --reload
```

3. **Uso**:
Abre en tu navegador `http://127.0.0.1:8000/`. Dentro del dashboard, presiona el botón **"Iniciar Scraping"**; este comando desencadenará el robot asíncrono y en cuestión de segundos las gráficas se visualizarán en tiempo real.
