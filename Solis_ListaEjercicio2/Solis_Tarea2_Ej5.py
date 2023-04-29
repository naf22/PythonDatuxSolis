"""".Crear una funcion que al mandar como parámetro un path me liste los elementos que
contiene esa carpeta ,en caso sea una carpeta llamar otra vez tu función que lista los
elementos de esa subcarpeta."""
import os
print("ANTES DE EJECUTAR,INGRESAR EL PATH O LA RUTA A LA FUNCION")
def listar_elementos(path):
    elementos = os.listdir(path)
    for elemento in elementos:
        """ruta del elemento que esta dentro de la carpeta"""
        elemento_path = os.path.join(path, elemento)

        """verficaremos si hay una carpeta dentro dl path que se  envio al inicio como parametro"""
        if os.path.isdir(elemento_path):
            """llamaremos nuevamente a la funcion y listara los elementos de la carpeta que fue hallada"""
            print("---------Elementos de la subcarpeta hallada---------")
            listar_elementos(elemento_path)
        else:
            print(elemento)
    

listar_elementos('D:\PruebaSolis')