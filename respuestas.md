## 🔐 Respuestas a la retroalimentación

### 1) Abuso del sistema para envío masivo de correos (spam)

Un atacante podría abusar de la funcionalidad de envío de correos automatizando solicitudes al sistema, utilizando scripts o bots para generar grandes volúmenes de emails en poco tiempo. Esto convertiría al sistema en una herramienta de envío de spam.

Las consecuencias serían críticas, ya que el servidor podría ser incluido en listas negras (blacklists), afectando su reputación y provocando que correos legítimos sean bloqueados o marcados como spam. Además, el envío masivo de correos consumiría recursos del servidor (CPU, memoria y ancho de banda), afectando la disponibilidad del servicio para usuarios legítimos.

Para mitigar este riesgo, se pueden implementar medidas como:

* Autenticación obligatoria para usar el servicio
* Rate limiting (limitación de solicitudes por usuario o IP)
* Validación de contenido y destinatarios
* Uso de CAPTCHA para evitar automatización
* Monitoreo y detección de comportamiento anómalo

---

### 2) Defensa contra múltiples procesos de scraping concurrentes

Un atacante podría explotar los endpoints del sistema para lanzar múltiples procesos de scraping simultáneamente, lo que consumiría excesivamente los recursos del servidor (CPU, memoria y red). Esto podría provocar una degradación del servicio o incluso una caída total (denegación de servicio).

El impacto principal sería la pérdida de disponibilidad del sistema, afectando a los usuarios legítimos y reduciendo el rendimiento general de la aplicación.

Para prevenir este tipo de ataques, se pueden aplicar varias estrategias:

* Implementar rate limiting por usuario o IP
* Controlar la concurrencia (limitar número de procesos simultáneos)
* Uso de colas de tareas (por ejemplo, Celery o Redis)
* Autenticación y autorización para acceder a los endpoints
* Monitoreo del sistema y alertas ante uso excesivo

Estas medidas permiten mantener el control sobre los recursos del sistema y asegurar la estabilidad y disponibilidad del servicio.
