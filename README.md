# Proyecto Final Python - Blog con Gestión de Libros

Este proyecto fue desarrollado como entrega final del curso de **Python** en el marco de la **Diplomatura en Data Science**.  
Consiste en una aplicación web desarrollada con el framework **Django**, que permite la gestión de usuarios, mensajería interna y administración de libros.

---

##  Funcionalidades principales

- Registro, inicio y cierre de sesión de usuarios.  
- Sección de **mensajes** entre usuarios.  
- CRUD de **libros** (crear, ver, editar y eliminar).  
- Campos de cada libro: título, autor, género, fecha de publicación, descripción y disponibilidad.  
- Editor enriquecido de texto (`ckeditor`) para la descripción.    
- Interfaz con sistema de autenticación (solo usuarios registrados pueden agregar o editar libros).  

---

## Tecnologías utilizadas

- **Python 3.14**
- **Django 6.0**
- **SQLite3**
- **HTML / CSS**
- **Bootstrap**
- **CKEditor**

---

## Estructura principal del proyecto
ENTREGAFINAL_GORLERO/
│
├── accounts/ # Manejo de usuarios y autenticación
├── books/ # CRUD de libros
├── messaging/ # Sistema de mensajería
├── mi_blog_final/ # Configuración principal del proyecto
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── db.sqlite3 # (Ignorado por .gitignore)
├── media/ # Imágenes subidas (ignorado por .gitignore)
├── manage.py
└── README.md

## ⚙️ Instalación y ejecución local

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/msolgorlero90/Python_ENTREGAFINAL_GORLERO.git
   cd Python_ENTREGAFINAL_GORLERO
   
2. Instalar dependencias:

bash
Copy code
pip install django django-ckeditor

3. Aplicar migraciones:
bash
Copy code
python manage.py makemigrations
python manage.py migrate

4. Iniciar el servidor:

bash
Copy code
python manage.py runserver

5. Acceder desde el navegador:

cpp
Copy code
http://127.0.0.1:8000/

## Credenciales de prueba
Usuario: gorlero  
Contraseña: gorlero123

## Autor
María Sol Gorlero
Diplomatura en Data Science – Proyecto Final Python
Buenos Aires, Argentina – 2025
