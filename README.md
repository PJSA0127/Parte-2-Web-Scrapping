# 🌐 Web Scraping - Quotes

## 📌 Descripción
Este proyecto implementa un sistema de web scraping para extraer citas desde un sitio web, almacenarlas y analizarlas mediante técnicas de procesamiento de datos.

Además, se incorporan medidas de seguridad para prevenir abusos del sistema.

---

## ⚙️ Funcionalidades

- Scraping de citas desde páginas web
- Almacenamiento en CSV
- Procesamiento y análisis de datos
- API con FastAPI
- Control de concurrencia
- Prevención de abuso

---

## 🛡️ Seguridad implementada

### 1) Prevención de spam

- Autenticación obligatoria
- Rate limiting por IP
- Validación de datos
- CAPTCHA
- Monitoreo de actividad

---

### 2) Protección contra scraping masivo

- Limitación de procesos concurrentes
- Uso de colas (Celery / Redis)
- Control de acceso
- Monitoreo del sistema

---

## 📊 Tecnologías

- Python
- FastAPI
- Pandas
- Requests
- BeautifulSoup
- Matplotlib
- Scikit-learn

---

## ▶️ Ejecución

```bash
pip install -r requirements.txt
python scraping.py
