from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/url")
async def url():
    return {"url": "xD"}

# ejecutar servidor uvicorn main:app --reload
# documentacion http://127.0.0.1:8000/docs