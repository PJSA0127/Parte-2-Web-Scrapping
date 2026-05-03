<<<<<<< HEAD
# 🌐 Web Scraping - Quotes

## 📌 Descripción

Script en Python que realiza **web scraping** desde una página pública para extraer frases y autores.

Los datos son procesados y guardados en un archivo CSV.

---

## 🌍 Página utilizada

https://quotes.toscrape.com/

---

## 📊 Datos extraídos

* Frases (quotes)
* Autores

---

## ⚙️ Instalación

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Ejecución

```bash
python scraping.py
```

---

## 📁 Resultado

Se genera un archivo:

```
quotes.csv
```

---

## 📄 Ejemplo de datos

| Frase                                | Autor           |
| ------------------------------------ | --------------- |
| “The world as we have created it...” | Albert Einstein |
| “It is our choices…”                 | J.K. Rowling    |

---

## 🚀 Tecnologías utilizadas

* Python
* Requests
* BeautifulSoup
* CSV

---

## 🧠 Proceso realizado

1. Se accede a la página web
2. Se analizan los elementos HTML
3. Se extraen frases y autores
4. Se limpian los datos
5. Se guardan en CSV

---
=======
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
>>>>>>> 4a327ec9c61118b700e415da9894c8d5e51f6e2f
