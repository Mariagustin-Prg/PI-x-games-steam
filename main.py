import pandas as pd
import ast
from functions import genres, juegos, early_access, specs, metascore, sentiment

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def initial():
    return "Welcome!"


@app.get("/genres/{anio}")
def genero(anio: str):
    return genres(anio)


@app.get("/games/{anio}")
def games(anio: str):
    return juegos(anio)


@app.get("/specs/{anio}")
def Especificaciones(anio: str):
    return specs(anio)


@app.get("/early_access/{anio}")
def Acceso_anticipado(anio: str):
    return early_access(anio)


@app.get("/sentiments/{anio}")
def Sentimientos(anio: str):
    return sentiment(anio)

@app.get("/metascore/{anio}")
def metascore_puntuación(anio: str):
    return metascore(anio)
