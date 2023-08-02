import pandas as pd
import ast

import numpy as np

def genres(año):
    """
    Esta función toma un año como entrada y devuelve un diccionario con los cinco géneros de videojuegos más comunes 
    en ese año, junto con la cantidad de veces que aparecen en el archivo 'genres.csv'.

    Parámetros:
        año (str o int): El año para el que se desea obtener los géneros más comunes de videojuegos. 
                         Debe estar en formato de cadena o entero.

    Retorna:
        dict: Un diccionario que contiene los cinco géneros más comunes de videojuegos en el año especificado.
              Cada clave representa un género y su valor es el número de veces que aparece en 'genres.csv'.

    Ejemplo:
        Supongamos que tenemos un archivo 'genres.csv' con información sobre videojuegos y se ejecuta la función
        genres("2000"). Devuelve el siguiente resultado:

        {
            "Action": 18,
            "Adventure": 8,
            "Strategy": 8,
            "Simulation": 7,
            "Casual": 6
        }

        Esto indica que en el año 2000, el género "Action" fue el más común con 18 apariciones, seguido de "Adventure" 
        y "Strategy" con 8 apariciones cada uno, y así sucesivamente.
    """
    import itertools
    import ast
    _df = pd.DataFrame(pd.read_csv("./csv to functions/genres.csv"))
    
    año = str(año)
    lines = _df[_df['release_date'].str.contains(año, case= False ,na= False)]

    transformation = []
    for registro in lines['genres']:
        try: 
            transformation.append(ast.literal_eval(registro))
        except ValueError:
            transformation.append([])
    lines['genres'] = transformation

    lista_generos = {}
    for registro in lines['genres']:
        for genre in registro:
            lista_generos[f'{genre}'] = 0

    for registro in lines['genres']:
        for genre in registro:
            lista_generos[f'{genre}'] += 1

    return dict(itertools.islice(dict(sorted(lista_generos.items(), key= lambda item: item[1], reverse= True)).items(), 5))

def juegos(año):
    """
    Esta función toma un año como entrada y devuelve una lista de los títulos de los videojuegos lanzados en ese año, 
    que están presentes en el archivo 'genres.csv'.

    Parámetros:
        año (str o int): El año para el cual se desean obtener los títulos de los videojuegos. 
                         Debe estar en formato de cadena o entero.

    Retorna:
        list: Una lista que contiene los títulos de los videojuegos lanzados en el año especificado y presentes en 'genres.csv'.

    Ejemplo:
        Supongamos que tenemos un archivo 'genres.csv' con información sobre videojuegos y se ejecuta la función
        juegos('2021'). Devuelve el siguiente resultado:

        ["Finding Paradise Soundtrack"]

        Esto indica que en el año 2021, el único videojuego cuyo título se encuentra en el archivo es 
        "Finding Paradise Soundtrack".
    """
    _df = pd.DataFrame(pd.read_csv("./csv to functions/genres.csv"))
    
    lines = _df[_df['release_date'].str.contains(año, case= False ,na= False)]
    lista_de_juegos = list(lines['title'])

    return lista_de_juegos

def specs(año):
    """
    Esta función toma un año como entrada y devuelve un diccionario con las cinco especificaciones más comunes de los
    videojuegos lanzados en ese año, que se encuentran presentes en el archivo 'specs.csv'.

    Parámetros:
        año (str o int): El año para el cual se desean obtener las especificaciones de los videojuegos. 
                         Debe estar en formato de cadena o entero.

    Retorna:
        dict: Un diccionario que contiene las cinco especificaciones más comunes de los videojuegos lanzados en el año
              especificado y presentes en 'specs.csv'. Cada clave representa una especificación y su valor es la cantidad 
              de veces que aparece en el archivo.

    Ejemplo:
        Supongamos que tenemos un archivo 'specs.csv' con información sobre especificaciones de videojuegos y se ejecuta
        la función specs(1998). Devuelve el siguiente resultado:

        {
            "Single-player": 50,
            "Multi-player": 17,
            "Captions available": 11,
            "Steam Cloud": 9,
            "Partial Controller Support": 4
        }

        Esto indica que en el año 1998, la especificación "Single-player" fue la más común con 50 apariciones en los 
        videojuegos, seguida de "Multi-player" con 17 apariciones, y así sucesivamente.
    """
    import itertools
    _df = pd.DataFrame(pd.read_csv("./csv to functions/specs.csv"))

    lines = _df[_df['release_date'].str.contains(año, case= True, na= False)]

    especificaciones = []
    for registro in lines['specs']:
        try:
            especificaciones.append(ast.literal_eval(registro))
        except ValueError:
            especificaciones.append([])

    dict_de_specs = {}
    for registro in especificaciones:
        for sp in registro:
            dict_de_specs[f'{sp}'] = 0

    for registro in especificaciones:
        for sp in registro:
            dict_de_specs[f'{sp}'] += 1

    return dict(itertools.islice(dict(sorted(dict_de_specs.items(), key= lambda item: item[1], reverse= True)).items(), 5))

def early_access(año):
    """
    Esta función toma un año como entrada y devuelve un diccionario con la cantidad de videojuegos con acceso anticipado 
    lanzados en ese año, según la información proporcionada en el archivo 'early_access.csv'.

    Parámetros:
        año (str o int): El año para el cual se desean obtener la cantidad de videojuegos con acceso anticipado.
                         Debe estar en formato de cadena o entero.

    Retorna:
        dict: Un diccionario que contiene el año proporcionado y la cantidad de videojuegos con acceso anticipado 
              lanzados en ese año, según la información del archivo 'early_access.csv'.

    Ejemplo:
        Supongamos que tenemos un archivo 'early_access.csv' con información sobre videojuegos en acceso anticipado 
        y se ejecuta la función early_access(2010). Devuelve el siguiente resultado:

        {
            "Año": "2010",
            "Cantidad de juegos con acceso anticipado": 0
        }

        Esto indica que en el año 2010, no se encontraron videojuegos con acceso anticipado en el archivo, ya que la 
        cantidad devuelta es 0.
    """
    _df = pd.DataFrame(pd.read_csv("./csv to functions/early_access.csv"))
    _df = _df[_df['release_date'].str.contains(año, case= False, na= False)]
    lines = _df[_df['early_access'] == True]

    return {
        'Año': año,
        'Cantidad de juegos con acceso anticipado' : lines['title'].shape[0]
    }

def sentiment(año):
    """
    Esta función toma un año como entrada y devuelve un diccionario con los cinco sentimientos más comunes asociados 
    a los videojuegos lanzados en ese año, según la información proporcionada en el archivo 'sentiments.csv'.

    Parámetros:
        año (str o int): El año para el cual se desean obtener los sentimientos asociados a los videojuegos.
                         Debe estar en formato de cadena o entero.

    Retorna:
        dict: Un diccionario que contiene los cinco sentimientos más comunes asociados a los videojuegos lanzados en 
              el año especificado, según la información del archivo 'sentiments.csv'. Cada clave representa un sentimiento 
              y su valor es la cantidad de veces que aparece en el archivo.

    Ejemplo:
        Supongamos que tenemos un archivo 'sentiments.csv' con información sobre sentimientos asociados a videojuegos y 
        se ejecuta la función sentiment(1996). Devuelve el siguiente resultado:

        {
            "Positive": 12,
            "Very Positive": 11,
            "Mostly Positive": 4,
            "Mostly Negative": 1
        }

        Esto indica que en el año 1996, el sentimiento más común asociado a los videojuegos fue "Positive" con 12 apariciones,
        seguido de "Very Positive" con 11 apariciones, y así sucesivamente.
    """
    import itertools
    _df = pd.DataFrame(pd.read_csv("./csv to functions/sentiments.csv"))
    lines = _df[_df['release_date'].str.contains(año, case= False, na= False)]

    dict_sentimientos = {}
    for registro in lines['sentiment']:
        dict_sentimientos[f'{registro}'] = 0

    for registro in lines['sentiment']:
        dict_sentimientos[f'{registro}'] += 1

    dicc = dict(sorted(dict_sentimientos.items(), key= lambda item: item[1], reverse= True))
    df_ = pd.DataFrame(data=dicc.values(), index= dicc.keys()).reset_index(drop= False)
    dicc2 = df_[df_['index'].str.contains("tive", na= False)]
    return dict(dicc2.head().values)

def metascore(año):
    """
    Esta función toma un año como entrada y devuelve un diccionario con los títulos de los videojuegos lanzados en ese 
    año, junto con su puntaje de Metascore más alto, según la información proporcionada en el archivo 'metascore.csv'.

    Parámetros:
        año (str o int): El año para el cual se desean obtener los títulos con sus puntajes de Metascore más altos.
                         Debe estar en formato de cadena o entero.

    Retorna:
        dict: Un diccionario que contiene los títulos de los videojuegos lanzados en el año especificado, junto con su 
              puntaje de Metascore más alto, según la información del archivo 'metascore.csv'. Cada clave representa el 
              título del videojuego y su valor es el puntaje de Metascore más alto.

    Ejemplo:
        Supongamos que tenemos un archivo 'metascore.csv' con información sobre puntajes de Metascore para videojuegos y 
        se ejecuta la función metascore(2012). Devuelve el siguiente resultado:

        {
            "Batman: Arkham City - Game of the Year Edition": 91,
            "Dishonored": 91,
            "Mark of the Ninja": 91,
            "XCOM: Enemy Unknown": 89
        }

        Esto indica que en el año 2012, los videojuegos "Batman: Arkham City - Game of the Year Edition", "Dishonored" y 
        "Mark of the Ninja" tienen el puntaje más alto de Metascore con 91, mientras que "XCOM: Enemy Unknown" tiene un 
        puntaje de 89.
    """
    import numpy as np
    _df = pd.DataFrame(pd.read_csv("./csv to functions/metascore.csv"))

    _df = _df[_df['release_date'].str.contains(año, case= False, na= False)]
    _df.sort_values('metascore', ascending=False, inplace= True)
    _df.drop(columns= 'release_date', inplace= True)
    _df.fillna(0, inplace= True)
    try:
        if _df.iloc[0,1] <= 1:
            return {}
    except IndexError:
        pass
    return dict(_df.head().values)