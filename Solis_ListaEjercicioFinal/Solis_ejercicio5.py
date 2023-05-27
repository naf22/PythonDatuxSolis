import requests
import sqlite3
import pandas as pd
import os

pd.set_option('display.max_rows', None) 
df = pd.read_csv('./properties_ar.csv',sep=',')
conexion=sqlite3.connect('bdproperties.db')
co=conexion.cursor()
crear_tabla="""
create table PROPERTIES_P5(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha VARCHAR(250),
    tipoventa  VARCHAR(250),
    tipocasa  VARCHAR(250),
    ciudad  VARCHAR(250),
    pais  VARCHAR(250),
    precio VARCHAR(250)
    )"""
co.execute("DROP TABLE IF EXISTS PROPERTIES_P5") 
co.execute(crear_tabla)
try:
   for i, row in df.iterrows():
      fecha=row[0]
      tipoventa=row[1]
      tipocasa=row[2]
      ciudad= row[3]
      pais=row[4]
      precio=row[5]
      insertParametetrizada="INSERT INTO PROPERTIES_P5(fecha, tipoventa, tipocasa, ciudad, pais, precio) values(?, ?, ?, ?, ?, ?)"
      dataParametrizada=(fecha, tipoventa, tipocasa, ciudad, pais, precio)
      co.execute(insertParametetrizada,dataParametrizada)
      conexion.commit()
except:
   print("hubo un error")
else:
   print("La inserción datos fue exitosa,revise la bdproperties")
   conexion.close()






