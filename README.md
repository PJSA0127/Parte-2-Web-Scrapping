# Web Scraping + Análisis de Datos

## Descripción
Este proyecto realiza web scraping sobre la página: https://quotes.toscrape.com/  
El objetivo es extraer citas, autores y etiquetas (tags), procesar los datos y generar archivos CSV listos para análisis.

## Tecnologías utilizadas
Python
Requests
BeautifulSoup
Pandas

## Funcionalidades
Extracción de datos desde múltiples páginas (paginación)
Limpieza de datos
Generación de dataset en CSV
Análisis de autores más frecuentes
Análisis de tags más utilizados

## Resultados
Al ejecutar el programa se genera automáticamente la carpeta data/ con los siguientes archivos:quotes.csv, top_authors.csv, top_tags.csv

## Ejecución del proyecto
```bash
pip install -r requirements.txt
python scraper.py
