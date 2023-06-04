## Metodologia
La metodologia utilizada para este proyecto fue con un enfoque pragmático ya que seguía las tareas punto a punto

## Prerrequisitos
* Tener instalada la version 3 de Python
* Tener instalado docker y docker-compose
* Tener instalado git
* Tener instalado postgres (en el caso que se use sin docker)

## Instalacion Mac/Linux (sin docker)
* Clonar el repositorio
* Crear un [entorno virtual](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) `python3 -m venv venv/`
* Activar el entorno virtual `source venv/bin/activate`
* Instalar dependencias `pip install -r requirements.txt`
* Crear base de datos con el nombre `pizzeria` y modificar las variables de la base de datos del archivo `settings.py` si son necesarias
* Correr migraciones `./manage.py migrate`
* Correr servidor `./manage.py runserver`
* Correr tests `./manage.py test`
* Ir a `http://localhost:8000/swagger/` para ver documentación de la API

## Consideraciones
* No hay un endpoint para agregar ingredientes a una pizza, esta funcionalidad ya esta incluida en la creacion de las pizzas (se debe pasar un array con los ids de los ingredientes que se quiere), la misma cosa para actualizar los ingredientes de la pizza, se actualiza la pizza y se pasa la lista de ingredientes actualizados
* Como los endpoints eran relativamente sencillos avance con el desarrollo antes que con las pruebas, pero si era de otra forma iba utilizar un desarrollo en base a tests (TDD)
* El repositorio se creo aproximadamente el 04/06/2023 a las 9:30 aproximadamente y se termino a las 04/06/2023 a las 15:50 con una hora de almuerzo aprox.