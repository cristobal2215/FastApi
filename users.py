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

@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id))==User:
        return {"error": "User already exists"}
    else:
        users_list.append(user)
        return user

@app.put("/user/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "User not found"}
    else:
        return user

@app.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error": "User has not deleted"}



def search_user(id: int):
    users= filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "User not found"}

