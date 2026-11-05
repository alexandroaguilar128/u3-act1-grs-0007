import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Alexandro Aguilar NC 0007

#crearemos nuestra tabla y la guardaremos con pandas
# tenemos 5 listas de redes sociales con 4 elementos por lista
fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkdin', 7277, False, 2012]
# Creamos una lista de listas (conformando la tabla)
lista_redes_sociales = [fb, twt, ig, wsp, tel, lkn]
# print(lista_redes_sociales)
# Utilizar pandas para organizar la tabla (dataframe o marco de datos)
# A cada columna le ponemos nombre
df_redes_sociales = pd.DataFrame(lista_redes_sociales,
                                 columns=['Nombre', 'Cantidad', 'Es_FB', 'Años'])
print(df_redes_sociales)
# creamos el archivo CSV y lo guardamos en CSV. to_csv permite el dataframe convertirse en csv para ser guardado
# df_redes_sociales.to_csv("redessociales.csv", index=False)
# Crear grafica de lineas 
# Donde X es nombre en el eje horizontal
# Donde Y es cantidad en el eje vertical
plt.plot(df_redes_sociales['Nombre'], df_redes_sociales['Cantidad'])
plt.title("Grafica redes sociales 0007")
plt.xlabel("Nombre de las redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
# Creamos una grafica de puntos
# Scatter crea la grafica de puntos
plt.scatter(df_redes_sociales['Nombre'], df_redes_sociales['Cantidad'])
plt.show()
# Grafica de barras
# bar crea la grafica de barras
plt.bar(df_redes_sociales['Nombre'], df_redes_sociales['Cantidad'])
plt.title("Redes sociales 0007")
plt.xlabel("Las redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
# Ordenar la grafica de barras de mayor a menor
# sort_vales permite anular el orden ascendente y ponerlo en orden descendente
df_rs_ordenar= df_redes_sociales.sort_values('Cantidad', ascending=False)
plt.bar(df_rs_ordenar['Nombre'], df_rs_ordenar['Cantidad'])
plt.show()
# Poniendo color a la grafica
# Color pues agrega color
df_rs_ordenar= df_redes_sociales.sort_values('Cantidad', ascending=False)
plt.bar(df_rs_ordenar['Nombre'], df_rs_ordenar['Cantidad'],
        color = ['r', 'b', 'g', 'm', 'y', 'c'])
plt.show()
# Grafica de pastel/pie
# Como el nombre lo dice .pie permite crear un grafico con forma de pie o pastel
# Labels permite agregar los nombres 
plt.pie(df_redes_sociales['Cantidad'],
        labels=df_redes_sociales['Nombre'])
plt.show()
print("Alexandro Aguilar NC 0007")
