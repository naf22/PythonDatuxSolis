"""5. para la pregunta 4 al importar la funciones usar el manejo de errores (try ,except) y en las
sentencias de “ else “ imprimir la ruta del directorio de trabajo os.getcwd() y en la sentencia
finally imprimir “proceso terminado
”"""

import os
class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        try:
            pais, lote, anio = self.codigo.split('-')
        except ValueError:
            return "Código de producto inválido"
        else:
            print("Ruta del directorio de trabajo:", os.getcwd())
            return f"Nombre: {self.nombre}\nCódigo: {self.codigo}\nPaís de origen: {pais}\nNúmero de lote: {lote}"

#


