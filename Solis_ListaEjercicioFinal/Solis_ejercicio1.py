import requests
import sqlite3
conexion=sqlite3.connect('bdsunat.db')
co=conexion.cursor()
crear_tabla="""
create table INFOSUNAT(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    compra VARCHAR(250),
    venta  VARCHAR(250),
    origen  VARCHAR(250),
    moneda  VARCHAR(250),
    fecha  VARCHAR(250)
    )""" 
co.execute("DROP TABLE IF EXISTS INFOSUNAT")
co.execute(crear_tabla)

def Extraer_info_insertardb():
        url = ' https://api.apis.net.pe/v1/tipo-cambio-sunat'
        r = requests.get(url)
        data=r.json()
        compra=data['compra']
        venta=data['venta']
        origen=data['origen']
        moneda=data['moneda']
        fecha=data['fecha']
        insertParametetrizada="insert into INFOSUNAT(compra,venta,origen,moneda,fecha) values(?,?,?,?,?)"
        dataParametrizada=(compra,venta,origen,moneda,fecha)
        co.execute(insertParametetrizada,dataParametrizada)
        print("Se realizo correctamente,verifique el registro en la bdsunat")
        conexion.commit()
        conexion.close()


Extraer_info_insertardb()
