import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df_1 = pd.read_csv ('data/Box Office Female Leads/movies.csv')
df_2 = pd.read_json('http://bechdeltest.com/api/v1/getAllMovies')
df_3 = pd.read_csv('data/dir_gender_genre.csv')

# Películas (1970-2013) con alguna protagonista femenina que pasan o suspenden el test de Bechdel.
data = df_1["binary"].value_counts()
colors = ["#F7EC66", "#E61A54"]
plt.figure(figsize=(8, 8))
plt.pie(data.values, labels=data.index, autopct='%1.2f%%', colors=colors)
p = plt.gcf()
title = 'Ratio de aprobados en el test de Bechdel, en películas con protagonistas femeninas'
plt.title(title)
plt.show()


# Películas (1874-2023) sacadas de la API de bechdeltest.
data = df_2["bechdel"].value_counts()
colors = ["#E61A54","#28A296"]
plt.figure(figsize=(8, 8))
plt.pie(data.values, labels=data.index, autopct='%1.2f%%', colors=colors)
p = plt.gcf()
title = 'Ratio de aprobados en películas de la API del test de Bechdel, independientemente de que haya protagonista femenina'
plt.title(title)
plt.show()


# Películas (1970-2013) con alguna protagonista femenina que pasan o suspenden el test de Bechdel.
data = df_1["binary"].value_counts()
colors = ["#F7EC66", "#E61A54"]
plt.figure(figsize=(8, 8))
plt.pie(data.values, labels=data.index, autopct='%1.2f%%', colors=colors)
p = plt.gcf()
title = 'Ratio de aprobados en el test de Bechdel, en películas con protagonistas femeninas'
plt.title(title)
plt.show()


'''Análisis de la variable "test_bechdel" en el DataFrame df_bech_def. Se utiliza para determinar si una película cumple con el
Test Bechdel en un gráfico de pastel, para mostrar la distribución de películas que pasan y no pasan el test. El gráfico representa dos
variables categóricas: PASS y FAIL'''

# ¿Cumple test Bechdel?
data = df_bech_def["test_bechdel"].value_counts()
colors = ["#28A296", "#E61A54"]
plt.figure(figsize=(8, 8))
plt.pie(data.values, labels=data.index, autopct='%1.2f%%', colors=colors)
p = plt.gcf()
plt.show()
print(f'De todos los datos de películas entre 1874 y 2023 el 54.89% pasarían el test y el 45.11% no')

# Histograma: distribución de datos en función del año, con una diferenciación de colores basada en la columna "test_bechdel".
colors = ["#F7EC66","#28A296"]
plt.figure(figsize=(8, 6))
sns.histplot(x="year", hue="test_bechdel", data = df_bech_def, palette=colors, binwidth=6, multiple = "dodge")
plt.show()



# Gráfico de barras apiladas, % de películas "PASS" y "FAIL" en función de los períodos
data = df_bech_def
# períodos
periods = [(1874, 1980), (1981, 2000), (2001, 2020), (2021, 2023)]
# Porcentaje de películas con "PASS" y porcentaje con "FAIL", por período
pass_percentages = []
fail_percentages = []

for period in periods:
    start_year, end_year = period
    subset = data[(data['year'] >= start_year) & (data['year'] <= end_year)]
    pass_percent = (subset['test_bechdel'] == 'PASS').mean()
    fail_percent = (subset['test_bechdel'] == 'FAIL').mean()
    pass_percentages.append(pass_percent)
    fail_percentages.append(fail_percent)

# DataFrame con %
period_labels = [f"{start}-{end}" for (start, end) in periods]
percentage_data = pd.DataFrame({'Period': period_labels, 'PASS': pass_percentages, 'FAIL': fail_percentages})
colors = ["#28A296","#E61A54"]
plt.figure(figsize=(10, 6))
sns.barplot(x="Period", y="PASS", data=percentage_data, color=colors[0], label="PASS")
sns.barplot(x="Period", y="FAIL", data=percentage_data, color=colors[1], bottom=percentage_data["PASS"], label="FAIL")
plt.xlabel("Period")
plt.ylabel("Percentage")
plt.legend(title="Test Result", loc="upper right")
plt.xticks(rotation=45)
plt.show()

# Crear data frame de df_bech_def (df_1+df_2) solo de películas de 2023
df_12_2023 = df_bech_def[df_bech_def['year'] == 2023]


# Unir df_3. 
'''Provisionalmente, el excel creado para incluir las columnas GENDER (género del/la director/a) y
GENRE (género de la película), son solo las películas del 2023, con el objetivo de poder continuar en el trabajo
con lo relativo a estas correlaciones, pero está pendiente hacer el dataframe completo.'''
df_bechdel_2023 = pd.merge(df_12_2023, df_3, on='title', how='outer')

# % de películas dirigidas por Male o Female (de entre las de 2023)

data = df_bechdel_2023["dir_gender"].value_counts()
colors = ["#F7EC66", "#E61A54"]
plt.figure(figsize=(8, 8))
plt.pie(data.values, labels=data.index, autopct='%1.2f%%', colors=colors)
p = plt.gcf()
plt.show()


# Correlación cumple Bechdel - Género de la director/a 
# gráfico de barras apiladas
colors = ["#28A296","#242A34"]
g = sns.catplot(x="dir_gender",
                hue="test_bechdel",
                kind="count",
                edgecolor=".6",
                orient="v",
                data=df_bechdel_2023,
                palette=colors)  # Establecer la paleta de colores
plt.title("Distribución de 'PASS' y 'FAIL' por Género Cinematográfico")
plt.show()



# Filtrar datos para M
colors = ["#28A296", "#242A34"]
male_data = df_bechdel_2023[df_bechdel_2023['dir_gender'] == 'M']
male_counts = male_data['test_bechdel'].value_counts()
plt.figure(figsize=(10, 5))
plt.pie(male_counts, labels=male_counts.index, autopct='%1.1f%%', colors=colors)
plt.title("Correlación 'cumple Bechdel' - Género del Directores (M)")
plt.show()

# Filtrar datos para F
female_data = df_bechdel_2023[df_bechdel_2023['dir_gender'] == 'F']
female_counts = female_data['test_bechdel'].value_counts()
plt.figure(figsize=(10, 5))
plt.pie(female_counts, labels=female_counts.index, autopct='%1.1f%%', colors=colors)
plt.title("Correlación 'cumple Bechdel' - Género del Directores (F)")
plt.show()

# Calcular el porcentaje de géneros
porcentaje = df_bechdel_2023['genre'].value_counts(normalize=True) * 100
plt.figure(figsize=(10, 5))
plt.hlines(y=porcentaje.index,
           xmin=0,
           xmax=porcentaje,
           color='#A5173D')
plt.plot(porcentaje, porcentaje.index, "o")
plt.xlabel('Porcentaje')
plt.title('Porcentaje de Géneros de Películas (2023)')

# gráfico de barras apiladas, % de pass y fail por género de pelis
df_plot = df_bechdel_2023.groupby(['test_bechdel', 'genre']).size().reset_index().pivot(columns='test_bechdel',index='genre',values=0)
# Calcular los porcentajes
df_plot_percentage = df_plot.div(df_plot.sum(axis=1), axis=0) * 100
colors = ["#F7EC66", "#E61A54"]
sns.set_palette(sns.color_palette(colors))
df_plot_percentage.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title("Test de Bechdel por género cinematográfico, %")
plt.xlabel("género cinematográfico")
plt.ylabel("%")
plt.xticks(rotation=45)
plt.show()


