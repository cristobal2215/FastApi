from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str

users_list= [User(id=1, name="Cristobal", surname="Rodenas", email="cristobalroden@hotmail.com"),
User(id=2, name="Italo", surname="Pereda", email="italopereda@hotmail.com"),
User(id=3, name="Rodrigo", surname="Torrez", email="rodrigotorrez@hotmail.com")]

@app.get("/usersjson")
async def usersjson():
    return [{"nombre": "Cristobal", "surname": "Rodenas", "email": "cristobalroden@hotmail.com"},
            {"nombre": "Italo", "surname": "Pereda", "email": "italopereda@hotmail.com"},
            {"nombre": "Rodrigo", "surname": "Torrez", "email": "rodrigotorrez@hotmail.com"}]

@app.get("/users")
async def users():
    return users_list
#path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

#query
@app.get("/user/")
async def user(id: int):
    return search_user(id)

def search_user(id: int):
    users= filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "User not found"}