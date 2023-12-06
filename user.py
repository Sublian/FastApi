from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

# inicia el server: uvicorn user:app --reload

# entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
              User(id=2, name="Moure", surname="Dev", url="https://mouredev.com", age=35),
              User(id=3, name= "Haakon", surname= "Dahlberg", url= "https://haakon.com", age= 33),
              User(id=4, name= "Luis", surname= "Gonzalez", url= "https://github.com/sublian", age= 37)]

@app.get("/usersjson")
async def usersjson():  # Creamos un JSON a mano
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35},
            {"name": "Moure", "surname": "Dev", "url": "https://mouredev.com", "age": 35},
            {"name": "Haakon", "surname": "Dahlberg", "url": "https://haakon.com", "age": 33},
            {"name": "Luis", "surname": "Gonzalez", "url": "https://github.com/sublian", "age": 37}]

# muestra los usuarios    
@app.get("/users")
async def users():
    return users_list

# Path
@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:        
        return list(users)[0]
    except:
        return {"error": "No existe ese usuario"}    


# Query       
@app.get("/user/")
async def user(id: int):
    return search_user(id)          

# agregamos un usuario
@app.post("/user/")                   
async def user(user: User):
    if type(search_user(user.id))==User:
        return {"error": "El usuario ya existe"}
    
    users_list.append(user)            
    return user

#actualizar usuario
@app.put("/user/")
async def user(user: User):
    found= False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index]=user
            found= True
            
    if not found:
        return {"Error": "No se ha actualizado el usuario"}
    return user

# eliminar usuario
@app.delete("/user/{id}")            
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            return {"Mensaje": "Usuario eliminado"}
    
    if not found:
        return {"Error": "No se ha eliminado el usuario"}
        
    
# funciones
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:        
        return list(users)[0]
    except:
        return {"error": "No existe ese usuario"}

