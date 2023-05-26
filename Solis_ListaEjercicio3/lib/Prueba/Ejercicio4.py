""""
4.Programa que tenga una clase Producto el cual solo tiene los atributo de nombre y codigo
el codigo tiene la siguiente estructura ‘PAIS-LOTE-AÑO’ ejemplo : ‘PERU-0001-2023’ crear
un método que permita imprimir el objeto de forma literal (__str__) y que me permita
identificar el país de origen , el numero de lote 
."""
class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
#el metodo split me permitira separar el contenido del codigo tenienendo como referencia el (-).
    def __str__(self):
        pais, lote, anio = self.codigo.split('-') 
        return f"Nombre: {self.nombre}\nCódigo: {self.codigo}\nPaís de origen: {pais}\nNúmero de lote: {lote}"
    

