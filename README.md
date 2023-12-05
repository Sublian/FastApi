# Hello Python

[![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.88.0+-00a393?style=for-the-badge&logo=fastapi&logoColor=white&labelColor=101010)](https://fastapi.tiangolo.com)
[![MongoDB](https://img.shields.io/badge/MongoDB-6.0+-00684A?style=for-the-badge&logo=mongodb&logoColor=white&labelColor=101010)](https://www.mongodb.com)
[![ChatGPT](https://img.shields.io/badge/ChatGPT-GPT--4-7CF178?style=for-the-badge&logo=openai&logoColor=white&labelColor=101010)](https://platform.openai.com)

# FastAPI - Prácticas y Recomendaciones

Bienvenido al repositorio de prácticas para el desarrollo con FastAPI en Python. Este documento proporciona información útil, ejemplos y recomendaciones para trabajar de manera efectiva con FastAPI.

## ¿Qué es FastAPI?

FastAPI es un moderno y rápido framework web para construir APIs con Python 3.7+ basado en estándares y tipado de datos. Ofrece un rendimiento excepcional y una interfaz de desarrollo fácil de usar.

## Instalación

Para comenzar, instala FastAPI y el servidor ASGI (por ejemplo, Uvicorn) utilizando pip:

```bash
pip install fastapi uvicorn
```

## Ejecutando la Aplicación
Puedes ejecutar tu aplicación FastAPI utilizando Uvicorn con el siguiente comando:

```bash
uvicorn main:app --reload
```
Asegúrate de reemplazar main con el nombre de tu archivo principal y app con la instancia de tu aplicación FastAPI.

## Ejemplos de Uso
### Definir Rutas y Operaciones
```bash
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "¡Hola, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}
```

## Validación de Datos
FastAPI utiliza la validación de tipos para los datos de entrada y salida automáticamente.

```bash
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return item
```


## Recomendaciones

Utiliza el sistema de dependencias y la inyección de dependencias de FastAPI para gestionar componentes de manera eficiente.
Aprovecha las capacidades de la documentación interactiva generada automáticamente en http://localhost:8000/docs.
Explora la integración sencilla con bibliotecas como SQLAlchemy, Tortoise-ORM, y OAuth2 para una funcionalidad extendida.

```bash
Instala las siguientes librerias para utilizar este repo:
fastapi
python-jose
passlib
bcrypt
pymongo
python-multipart
```

### Backend desde cero by MoureDev (autor del curso)

En este repo utilizare el curso de MoureDev en el que aprenderemos a utilizar Python para backend e implementaremos un API REST con autenticación, base de datos y desplegaremos el proyecto en un servidor real.
Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=27335
> Código: Directorio "Backend" en el proyecto

<a href="https://youtu.be/_y9qQZXE24A"><img src="http://i3.ytimg.com/vi/_y9qQZXE24A/maxresdefault.jpg" style="height: 50%; width:50%;"/></a>

* [Introducción](https://youtu.be/_y9qQZXE24A)
* [Lección 01 - ¿Qué es un backend?](https://youtu.be/_y9qQZXE24A?t=125)
* [Lección 02 - API y FastAPI](https://youtu.be/_y9qQZXE24A?t=834)
* [Lección 03 - Type Hints](https://youtu.be/_y9qQZXE24A?t=1810)
* [Lección 04 - Configuración FastAPI](https://youtu.be/_y9qQZXE24A?t=2629)
* [Lección 05 - Hola mundo](https://youtu.be/_y9qQZXE24A?t=3504)
* [Lección 06 - Operación GET](https://youtu.be/_y9qQZXE24A?t=5382)
* [Lección 07 - Peticiones HTTP](https://youtu.be/_y9qQZXE24A?t=5925)
* [Lección 08 - Creación API](https://youtu.be/_y9qQZXE24A?t=6099)
* [Lección 09 - Path y Query](https://youtu.be/_y9qQZXE24A?t=7510)
* [Lección 10 - Operaciones POST, PUT y DELETE](https://youtu.be/_y9qQZXE24A?t=8529)
* [Lección 11 - HTTP status codes](https://youtu.be/_y9qQZXE24A?t=11072)
* [Lección 12 - Routers](https://youtu.be/_y9qQZXE24A?t=12475)
* [Lección 13 - Recursos estáticos](https://youtu.be/_y9qQZXE24A?t=13618)
* [Lección 14 - Autorización OAuth2](https://youtu.be/_y9qQZXE24A?t=14094)
* [Lección 15 - OAuth2 JWT](https://youtu.be/_y9qQZXE24A?t=17664)
* [Lección 16 - MongoDB](https://youtu.be/_y9qQZXE24A?t=20480)
* [Lección 17 - MongoDB Atlas](https://youtu.be/_y9qQZXE24A?t=25470)
* [Lección 18 - Despliegue en Deta *](https://youtu.be/_y9qQZXE24A?t=27335)
* [Próximos pasos](https://youtu.be/_y9qQZXE24A?t=28484)

***ACTUALIZACIÓN Sobre la lección 18:** Deta ha actualizado ligeramente su servicio de despliegue de aplicaciones con FastAPI. Tienes toda la documentación [aquí](https://deta.space/docs/en/quickstart-guides/python#fastapi). También han creado una [guía de migración](https://deta.space/migration/guides/migrate-a-micro/).

## Enlaces de interés

* [Web oficial de Python](https://www.python.org/)
* [Tutorial oficial de Python en Español](https://docs.python.org/es/3/tutorial/index.html)
* [Repo 30 días de Python](https://github.com/Asabeneh/30-Days-Of-Python)
* [Juego Codédex para aprender Python](https://www.codedex.io/)
* [Visual Studio Code](https://code.visualstudio.com/): El editor que estoy usando
* [FastAPI](https://fastapi.tiangolo.com/es/): El framework para crear nuestra API Backend
* [MongoDB](https://www.mongodb.com/): La base de datos que utiliza nuestro backend
* [Deta](https://www.deta.sh/): Para desplegar nuestra API en la nube

#### Puedes apoyar mi trabajo haciendo "☆ Star" en el repo

## Contribuciones
Siéntete libre de contribuir a este repositorio con ejemplos, prácticas y mejoras. ¡Tu colaboración es bienvenida!

## Licencia
Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.
Este README proporciona una breve introducción a FastAPI, instrucciones de instalación, ejemplos de código y recomendaciones para el desarrollo. Puedes personalizar y expandir este documento según las necesidades específicas de tu proyecto. ¡Espero que sea útil!

### En mi perfil de GitHub tienes más información

[![Web](https://img.shields.io/badge/GitHub-Sublian-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/sublian)
