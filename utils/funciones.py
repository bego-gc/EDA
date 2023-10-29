import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

import urllib,json
df_2 = pd.read_json('http://bechdeltest.com/api/v1/getAllMovies')


'''En el data frame 2, una puntuación Bechdel inferior a 3 significa que la película no pasó el test Bechdel, 
y una puntuación Bechdel de 3 significa que la película lo aprobó.'''

# Asignar "FAIL" o "PASS" según el valor en la columna "rating"
def asignar_bechdel(row):
    if row['rating'] < 3:
        return "FAIL"
    elif row['rating'] == 3:
        return "PASS"
    else:
        return None

# Crea la columna "bechdel"
df_2['bechdel'] = df_2.apply(asignar_bechdel, axis=1)






