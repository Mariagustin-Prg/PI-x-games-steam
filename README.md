# Proyecto de regresión de precios - Documentación

Este repositorio contiene un proyecto que utiliza FastAPI para construir una API que proporciona información sobre juegos y predicciones de precios. A continuación se detallan las rutas disponibles y su funcionalidad.

## Contenido

- [Descripción](#descripción)
- [Deploy](#Deploy)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Rutas](#rutas)
- [Funciones](#funciones-personalizadas)
- [Contribuciones](#contribuciones)


## Descripción

Este proyecto utiliza FastAPI para crear una API que brinda información sobre géneros de juegos, detalles de juegos, acceso anticipado, especificaciones, puntuación de metascore y análisis de sentimientos. Además, se ha entrenado un modelo de predicción de precios que utiliza estas características para predecir el precio de un juego.

## Deploy
Acceso al deploy de este repositorio en render: [Link a Render](https://steam-games-information.onrender.com/)

## Requisitos

- Python 3.x
- FastAPI
- Pandas
- Funciones personalizadas (genres, juegos, early_access, specs, metascore, sentiment)
- Modelo entrenado (predict_price)
- Scikit-learn

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias utilizando el siguiente comando:

```
pip install -r requirements.txt
```

## Uso

1. Ejecuta la aplicación FastAPI con el siguiente comando:

```
uvicorn main:app --host 0.0.0.0 --port 8000
```

2. Abre tu navegador o utiliza herramientas como cURL o Postman para acceder a las rutas de la API.

## Rutas

- `/`: Ruta de bienvenida.
- `/genres/{anio}`: Obtiene información sobre géneros de juegos para el año especificado.
- `/games/{anio}`: Obtiene detalles de juegos para el año especificado.
- `/specs/{anio}`: Obtiene especificaciones de juegos para el año especificado.
- `/early_access/{anio}`: Obtiene información sobre acceso anticipado para el año especificado.
- `/sentiments/{anio}`: Realiza un análisis de sentimientos para el año especificado.
- `/metascore/{anio}`: Obtiene puntuación de metascore para el año especificado.
- `/prediction_model/{generos}/{metascore}/{tags}/{access_e}`: Realiza una predicción de precio utilizando un modelo entrenado.

## Funciones Personalizadas

### `genres(año)`

Esta función toma un año como entrada y devuelve un diccionario con los cinco géneros de videojuegos más comunes en ese año, junto con la cantidad de veces que aparecen en el archivo 'genres.csv'.

```python
# Ejemplo de uso
generos_2000 = genres("2000")
print(generos_2000)
```

### `juegos(año)`
Esta función toma un año como entrada y devuelve una lista de los títulos de los videojuegos lanzados en ese año, que están presentes en el archivo 'genres.csv'.

```python
# Ejemplo de uso
juegos_2021 = juegos('2021')
print(juegos_2021)
```

### specs(año)
Esta función toma un año como entrada y devuelve un diccionario con las cinco especificaciones más comunes de los videojuegos lanzados en ese año, que se encuentran presentes en el archivo 'specs.csv'.

```python
# Ejemplo de uso
especificaciones_1998 = specs(1998)
print(especificaciones_1998)
```

### `early_access(año)`
Esta función toma un año como entrada y devuelve un diccionario con la cantidad de videojuegos con acceso anticipado lanzados en ese año, según la información proporcionada en el archivo 'early_access.csv'.

```python
# Ejemplo de uso
acceso_anticipado_2010 = early_access(2010)
print(acceso_anticipado_2010)
```

### `sentiment(año)`
Esta función toma un año como entrada y devuelve un diccionario con los cinco sentimientos más comunes asociados a los videojuegos lanzados en ese año, según la información proporcionada en el archivo 'sentiments.csv'.


```python
# Ejemplo de uso
sentimientos_1996 = sentiment(1996)
print(sentimientos_1996)
```

### `metascore(año)`
Esta función toma un año como entrada y devuelve un diccionario con los títulos de los videojuegos lanzados en ese año, junto con su puntaje de Metascore más alto, según la información proporcionada en el archivo 
'metascore.csv'.

```python
# Ejemplo de uso
puntajes_metascore_2012 = metascore(2012)
print(puntajes_metascore_2012)
```

## Contribuciones
Contribuciones y mejoras son bienvenidas. Si deseas contribuir, realiza los siguientes pasos:

Realiza un "fork" de este repositorio.
Crea una nueva rama para tus cambios.
Realiza tus modificaciones y mejoras.
Envía una solicitud de extracción describiendo tus cambios.
Licencia
Este proyecto está bajo la Licencia MIT.



