from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles


app = FastAPI()

#routers
app.include_router(products.router)
app.include_router(users.router)
app.mount('/static', StaticFiles(directory='static', name='static'))

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/url")
async def url():
    return {"url": "xD"}

# ejecutar servidor uvicorn main:app --reload
# documentacion http://127.0.0.1:8000/docs