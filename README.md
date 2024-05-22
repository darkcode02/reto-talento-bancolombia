# Proyecto Talento Bancolombia

Este repositorio contiene el código fuente y la documentación para el proyecto "Reto Talento Bancolombia". Este proyecto tiene como objetivo desarrollar una aplicación web para gestionar guiones de producción.

## Características

- Permite a los usuarios registrarse e iniciar sesión.
- Los usuarios pueden crear, ver, editar y eliminar guiones de producción.
- Los guiones pueden incluir título, descripción, posición del actor en la escena y una marca de importancia.
- Los usuarios pueden marcar un guion como completado.
- Interfaz de usuario intuitiva y fácil de usar.

## Tecnologías utilizadas

- Django: un framework web de alto nivel escrito en Python.
- HTML y CSS: para el diseño y la presentación de la interfaz de usuario.
- SQLite: una base de datos ligera y fácil de usar para el almacenamiento de datos en desarrollo.
- Git y GitHub: para el control de versiones y la colaboración en equipo.

## Instalación

1. Clona este repositorio en tu máquina local:

bash
git clone https://github.com/darkcode02/darkcode02-reto-talento-b-.git

    Crea un entorno virtual y activa el entorno virtual:

bash

python -m venv env
source env/bin/activate  # En sistemas Unix/Linux
env\Scripts\activate     # En sistemas Windows

    Instala las dependencias del proyecto:

bash

pip install -r requirements.txt

    Realiza las migraciones de la base de datos:

bash

python manage.py migrate

    Inicia el servidor de desarrollo:

bash

python manage.py runserver

    Accede a la aplicación en tu navegador web en la dirección http://localhost:8000.

Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

    Haz un fork del repositorio.
    Clona tu fork en tu máquina local.
    Crea una nueva rama para realizar tus cambios.
    Haz tus modificaciones y asegúrate de que los cambios pasen las pruebas.
    Haz commit de tus cambios y haz push a tu repositorio en GitHub.
    Envía un pull request desde tu rama hacia la rama principal del repositorio original.




Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto con el equipo de desarrollo a través de las Issues de GitHub o por correo electrónico a tupabloarias12345@gmail.com.


Este archivo README.md proporciona toda la información necesaria para entender, instalar y contribuir al proyecto en un formato Markdown fácil de leer y mantener.
