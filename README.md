# **OptiCall** 📞🔮  
> Sistema de Gestión de Workforce para Centros de Contacto  

**OptiCall** es una plataforma diseñada para optimizar la gestión de agentes, pronosticar demanda y mejorar la eficiencia operativa en centros de contacto. Construida con **Flask**, integra análisis predictivo, monitoreo en tiempo real y reportes detallados.  

## **📌 Características Principales**  
✅ **Gestión de Turnos**: Creación, asignación y consulta de horarios de agentes.  
✅ **Pronóstico de Demanda**: Predicciones con **Prophet** basadas en datos históricos.  
✅ **Monitoreo en Tiempo Real**: Seguimiento de actividad de agentes con **Flask-SocketIO**.  
✅ **Autenticación Segura**: Tokens **JWT** y control de accesos por roles.  
✅ **Reportes y Analíticas**: Visualización de métricas clave.  
✅ **API RESTful**: Endpoints optimizados para integraciones con terceros.  
✅ **Tareas en Segundo Plano**: Uso de **Celery** para procesamiento asincrónico.  

---

## **🛠️ Tecnologías Utilizadas**
| Componente            | Tecnología |
|-----------------------|-----------|
| **Backend**         | Flask |
| **Base de Datos**   | PostgreSQL / SQLite (para desarrollo) |
| **Autenticación**   | Flask-JWT-Extended |
| **ORM**            | SQLAlchemy |
| **Machine Learning** | Prophet (para predicción de llamadas) |
| **Tareas Asíncronas** | Celery + Redis |
| **Monitoreo** | Prometheus + Grafana |
| **WebSockets** | Flask-SocketIO |
| **Pruebas** | PyTest |

---

## **📂 Estructura del Proyecto**
```plaintext
.
├── opticall
│   ├── application        # Interfaz de usuario y controladores
│   │   ├── routes         # Definición de rutas y controladores
│   │   ├── static         # Archivos estáticos (CSS, JS, imágenes)
│   │   └── templates      # Plantillas HTML (Jinja)
│   ├── __init__.py        # Inicialización de la aplicación Flask
│   ├── __main__.py        # Punto de entrada de la aplicación
│   └── src
│       ├── modules        # Módulos de negocio (pronóstico, planificación, monitoreo)
│       └── shared         # Utilidades y lógica compartida
├── pyproject.toml         # Gestión de dependencias con Poetry
├── README.md              # Documentación del proyecto
└── tree.txt               # Estructura del proyecto

```

---

## **🚀 Instalación y Configuración**
### **1️⃣ Clonar el Repositorio**
```sh
git clone https://github.com/tuusuario/opticall.git
cd opticall
```

### **2️⃣ Crear un Entorno Virtual**
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### **3️⃣ Instalar Dependencias**
```sh
pip install -r requirements.txt
```

### **4️⃣ Configurar Variables de Entorno**
Crear un archivo `.env` en la raíz del proyecto:
```plaintext
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=supersecretkey
DATABASE_URL=postgresql://usuario:password@localhost/opticall_db
JWT_SECRET_KEY=superjwtkey
REDIS_URL=redis://localhost:6379/0
```

### **5️⃣ Inicializar la Base de Datos**
```sh
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### **6️⃣ Ejecutar la Aplicación**
```sh
flask run
```
Accede en: **http://127.0.0.1:5000** 🚀  

---

## **🛡️ Autenticación y Seguridad**
OptiCall utiliza **JWT (JSON Web Tokens)** para autenticación.  
Ejemplo de login:  
```sh
curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d '{"username": "admin", "password": "admin123"}'
```
Respuesta esperada:
```json
{"access_token": "eyJhbGciOiJIUzI1..." }
```
Este token debe enviarse en cada solicitud protegida:  
```sh
curl -X GET http://127.0.0.1:5000/protected -H "Authorization: Bearer <TOKEN>"
```

---

## **📡 API Endpoints**
| Método | Ruta | Descripción |
|--------|------|-------------|
| `POST` | `/login` | Autenticación con usuario y contraseña |
| `GET` | `/shifts` | Obtener turnos de agentes |
| `POST` | `/shifts` | Crear un nuevo turno |
| `POST` | `/predict` | Generar pronósticos de demanda |
| `GET` | `/realtime` | Obtener estado en tiempo real |

---

## **📊 Pronóstico de Demanda con Prophet**
OptiCall utiliza **Prophet** para prever la carga de trabajo con base en datos históricos.  
Ejemplo de petición:
```sh
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '[
    {"ds": "2025-01-01", "y": 150},
    {"ds": "2025-01-02", "y": 200}
]'
```
Respuesta esperada:
```json
[
    {"ds": "2025-01-03", "yhat": 180},
    {"ds": "2025-01-04", "yhat": 210}
]
```

---

## **🛠️ Pruebas y Desarrollo**
Ejecutar pruebas unitarias con **PyTest**:
```sh
pytest tests/
```
Correr pruebas de carga con **Locust**:
```sh
locust -f tests/load_test.py --host http://127.0.0.1:5000
```

---

## **🔧 Despliegue**
### **🔹 Opción 1: Gunicorn**
```sh
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
```

### **🔹 Opción 2: Docker**
```sh
docker build -t opticall .
docker run -d -p 5000:5000 --env-file .env opticall
```

---

## **📈 Monitoreo con Prometheus**
OptiCall expone métricas en `/metrics` para monitoreo con Prometheus y Grafana.

```sh
pip install prometheus-flask-exporter
```

Ejemplo de integración en `__init__.py`:
```python
from prometheus_flask_exporter import PrometheusMetrics
metrics = PrometheusMetrics(app)
metrics.info("opticall", "OptiCall Workforce Management System", version="1.0")
```

---

## **📖 Roadmap**
🔹 Mejorar predicciones con modelos avanzados de ML  
🔹 Integración con sistemas ACD (Cisco, Avaya)  
🔹 Panel de control interactivo con Dash o React  

---

## **👨‍💻 Contribución**
¡Toda ayuda es bienvenida! Si deseas contribuir, abre un **issue** o envía un **pull request**.  

1. **Fork** el repositorio  
2. Crea una nueva rama (`git checkout -b feature-nueva`)  
3. Haz cambios y haz commit (`git commit -m "Nueva funcionalidad"`)  
4. Sube los cambios (`git push origin feature-nueva`)  
5. Abre un **Pull Request** 🚀  

---

## **📜 Licencia**
Proyecto bajo licencia **MIT**.  

---

## **💬 Contacto**
📧 Email: fernando@opticall.com  
🌐 Web: [opticall.com](https://opticall.com)  

🚀 **¡Optimiza tu centro de contacto con OptiCall!** 🚀