import pandas as pd
import numpy as np
import ast

# Importamos las librerías de scikit-learn que utilizaremos en este proyecto.
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

df = pd.read_json("processed_data.json")

encoder = OneHotEncoder(handle_unknown='ignore')

values_encoded = encoder.fit_transform(df['values'].values.reshape(-1,1))
price_array = df['price'].values.reshape(-1, 1)

# Sepramos los datos ne datos de entrenamiento y de testeo
X_train, X_test, y_train, y_test = train_test_split(values_encoded, price_array, test_size= 0.2, random_state= 42)

# Creamos el modelo Ridge
model_ridge = Ridge(alpha= 0.75)
# Lo entrenamos
model_ridge.fit(X_train, y_train)
# Obtenemos el error cuadrático medio
y_pred = model_ridge.predict(X_test)
mse = mean_squared_error(y_pred, y_test)


def predict_price(generos=None, metascore=None, tags=None, access_e=False):
    if generos is not None:
        generos = list(generos)
        generos = " | ".join(generos)
    elif generos is None:
        generos = ""
    if tags is not None:
        tags = list(tags)
        tags = " | ".join(tags)
    elif tags is None:
        tags= ""
    if metascore is None:
        metascore = ""

    lista_values = []
    try:
        lista_values.append(generos)
    except TypeError:
        lista_values.append("")
    try:
        lista_values.append(str(metascore))
    except TypeError:
        pass
    try:
        lista_values.append(tags)
    except TypeError:
        lista_values.append("")
    
    lista_values.append(str(access_e))

    value_2 = " / ".join(lista_values)
    value_f = np.array(value_2).reshape(-1,1)

    encod_value = encoder.transform(value_f)
    predict = model_ridge.predict(encod_value)
    return {
        "Predict price" : predict[0][0],
        "MSE" : mse
    }