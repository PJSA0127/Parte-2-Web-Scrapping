# 🌐 Web Scraping - Quotes

## 📌 Descripción
Este proyecto implementa un sistema de web scraping para extraer citas desde un sitio web, almacenarlas y analizarlas mediante técnicas de procesamiento de datos.

Además, se incorporan medidas de seguridad y buenas prácticas para evitar abusos del sistema.

---

## ⚙️ Funcionalidades

- Scraping de citas desde páginas web
- Almacenamiento en CSV
- Procesamiento y análisis de datos
- Implementación de endpoints con FastAPI
- Control de concurrencia en scraping
- Prevención de abuso del sistema

---

## 🛡️ Seguridad implementada

### 1) Prevención de spam (envío masivo de correos)

- Autenticación obligatoria
- Rate limiting por IP o usuario
- Validación de contenido
- Uso de CAPTCHA
- Monitoreo de actividad sospechosa

---

### 2) Protección contra scraping masivo

- Limitación de procesos concurrentes
- Uso de colas de tareas (Celery / Redis)
- Control de acceso a endpoints
- Monitoreo de uso de recursos

---

## 📊 Tecnologías utilizadas

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