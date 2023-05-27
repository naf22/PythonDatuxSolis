"""
4.Realizar con pandas carga un archivos (csv, excel ,json)
4.1 Realizar una operación al archivo (ya sea filtro ,merge ,añadir columna con lógica ,etc)
"""
print("""4.1.""")
import pandas as pd
import os

pd.set_option('display.max_rows', None) 

df = pd.read_csv('./properties_ar.csv',sep=',')
print(df.head(10))
print("-----el archivo csv tiene las columnas: id,fecha,tipoventa,tipocasa,ciudad,pais,precio")

filtro=input("ingrese la columna que desea filtrar: ")
def filtrar_columna():
    for c in df.columns:
        if  c==filtro :
            print(df[c].head(10)) 

filtrar_columna()
