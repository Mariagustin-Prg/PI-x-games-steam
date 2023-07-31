import pandas as pd
import ast

import numpy as np

def genres(año):

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
    _df = pd.DataFrame(pd.read_csv("./csv to functions/genres.csv"))
    
    lines = _df[_df['release_date'].str.contains(año, case= False ,na= False)]
    lista_de_juegos = list(lines['title'])

    return lista_de_juegos

def specs(año):
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
    _df = pd.DataFrame(pd.read_csv("./csv to functions/early_access.csv"))
    _df = _df[_df['release_date'].str.contains(año, case= False, na= False)]
    lines = _df[_df['early_access'] == True]

    return {
        'Año': año,
        'Cantidad de juegos con acceso anticipado' : lines['title'].shape[0]
    }

def sentiment(año):
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
    _df = pd.DataFrame(pd.read_csv("./csv to functions/metascore.csv"))

    _df = _df[_df['release_date'].str.contains(año, case= False, na= False)]
    _df.sort_values('metascore', ascending=False, inplace= True)
    _df.drop(columns= 'release_date', inplace= True)
    return dict(_df.head().values)