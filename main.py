
from fastapi import FastAPI
app = FastAPI()

#se crea un funcuion para mostrar los datos de la primera pregunta " Año con más carreras "
@app.get("/uno")
async def  uno():
    return"hola"
    