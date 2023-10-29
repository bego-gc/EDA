import pandas as pd
import urllib,json

df_1 = pd.read_csv ('data/Box Office Female Leads/movies.csv')
df_2 = pd.read_json('http://bechdeltest.com/api/v1/getAllMovies')
df_3 = pd.read_csv('data/dir_gender_genre.csv')

# Indicar nuevo index
df_1.set_index('index', inplace = True) 

# Concatenar df 1, df 2
df_12 = pd.concat([df_1, df_2])

# Quitar NaN
df_12 = df_12.fillna('')

# Combinar columnas 'binary' y 'bechdel' en columna 'test_bechdel'
df_12['test_bechdel'] = df_12['binary'].astype(str) + df_12['bechdel'].astype(str)

# eliminar columnas y asignar a df_bech12
df_bech12 = df_12.drop(['test','clean_test','code','imdb', 'budget', 'domgross', 'intgross',	'budget_2013$','domgross_2013$','intgross_2013$','period code','decade code','imdbid','id', 'binary','rating','bechdel'], axis=1)

# Reemplazar '&#39;' por (')
df_bech12['title'] = df_bech12['title'].str.replace('&#39;', "'")
# Reemplazar '&amp;' por (and)
df_bech12['title'] = df_bech12['title'].str.replace('&amp;', "and")
# Reemplazar '"' por ( )
df_bech12['title'] = df_bech12['title'].str.replace('"', "")
# Reemplazar '&eacute;' por é
df_bech12['title'] = df_bech12['title'].str.replace('&eacute;', "é")
# Reemplazar "" por ___
df_bech12['title'] = df_bech12['title'].str.replace('"', "")


# Verificar duplicados.
duplicados = df_bech12[df_bech12.duplicated(subset="title", keep=False)]
# Eliminar duplicados en base a la columna "title"
df_bech_def = df_bech12.drop_duplicates(subset="title")

# Limpiar duplicados encontrados al editar en excel:
# Eliminar fila con index 10090
df_bech_def = df_bech_def.drop(10090)
# Eliminar fila con index 10101
df_bech_def = df_bech_def.drop(10101)
# Eliminar fila con index 10104
df_bech_def = df_bech_def.drop(10104)


# ...


import funciones
import visual
