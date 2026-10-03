# 🏠 Portal Inmobiliario — Django & PostgreSQL

Aplicación web Full Stack desarrollada en **Python y Django** que permite conectar a **arrendadores** (quienes publican y administran sus propiedades) con **arrendatarios** (quienes exploran el catálogo disponible filtrando por región y comuna de Chile).

## 🚀 Características Principales
* **Autenticación y Roles de Usuario:** Registro e inicio de sesión extendido mediante modelo `Perfil` (`Arrendador` y `Arrendatario`) con control de acceso en vistas y plantillas.
* **Operaciones CRUD con ORM:** Creación, lectura, actualización y eliminación de inmuebles conectados a una base de datos relacional **PostgreSQL**.
* **Filtro Geográfico Dinámico:** Búsqueda combinada en tiempo real por **Región** y **Comuna** en el catálogo de propiedades disponibles mediante peticiones `GET`.
* **Interfaz Responsiva:** Diseño adaptable a computadores y dispositivos móviles utilizando **Bootstrap 5**, herencia de plantillas (`base.html`) y formularios estilizados (`ModelForm`).

## 🛠️ Tecnologías Utilizadas
* **Backend:** Python 3, Django
* **Base de Datos:** PostgreSQL
* **Frontend:** HTML5, CSS3, Bootstrap 5

## ⚙️ Instalación y Ejecución Local
1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/TU_USUARIO/portal-inmobiliario-django.git](https://github.com/TU_USUARIO/portal-inmobiliario-django.git)