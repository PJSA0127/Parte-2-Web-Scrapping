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
