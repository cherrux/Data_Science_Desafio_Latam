#1. Importar la base de datos athlete_events.csv , y reportar la cantidad de registros (filas) y
#de campos (columnas). El resultado debe guardarse en una variable llamada ejercicio_1 .
#tip: Puede hacer uso de .shape para esto.

import pandas as pd
import numpy as np

df = pd.read_csv("athlete_events.csv")
ejercicio_1=df.shape
ejercicio_1

#2. Reportar cuántas competencias se han realizado a lo largo del tiempo. El resultado debe ser
#un número entero y debe guardarse en una variable llamada ejercicio_2 

ejercicio_2=len(df["Games"].value_counts())
ejercicio_2

#3 Reportar el porcentaje (número entre 0 y 1) de atletas que participaron tanto en los juegos
#olímpicos de Verano como en los de Invierno. El resultado debe guardarse en una variable
#llamada ejercicio_3 .
ejercicio_3 = round((df['ID'].groupby(df['Medal']).count() / df['Name'].count()), 2)
ejercicio_3

#4. Informar dónde fue la primera celebración de un Juego Olímpico de Verano. El resultado debe
#guardarse en una variable llamada ejercicio_4 .
#tip: Investige sobre las funciones min() y unique() de una Serie de pandas.

df_Summer = df[df['Season'] == 'Summer']
ejercicio_4 =((df_Summer[df_Summer['Year'] == df_Summer['Year'].min()]['City']).unique()),(df_Summer[df_Summer['Year'] == df_Summer['Year'].min()]["Year"]).unique()
ejercicio_4

#5 Informar dónde fue la primera celebración de un Juego Olímpico de Invierno. El resultado
#debe guardarse en una variable llamada ejercicio_5 .

df_Winter = df[df['Season'] == 'Winter']
ejercicio_5 =((df_Winter[df_Winter['Year'] == df_Winter['Year'].min()]['City']).unique()),(df_Winter[df_Winter['Year'] == df_Winter['Year'].min()]["Year"]).unique()
ejercicio_5


#6 Reportar los 10 primeros países con mayor cantidad de atletas participantes a lo largo de los
#juegos. El resultado debe guardarse en una variable llamada ejercicio_6 .

ejercicio_6 = ((df.loc[:, ["Name", "Team"]]).groupby('Team')['Name'].nunique().reset_index()).sort_values('Name', ascending=False).head(10)
ejercicio_6

#7 Reportar el porcentaje de medallas asignadas (oro, bronce, plata). El resultado debe
#guardarse en una variable llamada ejercicio_7

df_medallas_nan = df[df["Medal"].isnull() != True]
ejercicio_7 = round((df_medallas_nan['ID'].groupby(df_medallas_nan['Medal']).count() / df['Medal'].count()), 2)
ejercicio_7

#8 Reportar cuáles fueron los países participantes en las primeras olimpiadas de verano. El
#resultado debe guardarse en una variable llamada ejercicio_8

ejercicio_8 =((df_Summer[df_Summer['Year'] == df_Summer['Year'].min()]['Team']).unique())
ejercicio_8
