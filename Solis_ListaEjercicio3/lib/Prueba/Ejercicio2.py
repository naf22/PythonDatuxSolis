""""2. Una tienda de autopartes necesita un programa para catalogar sus productos ,crear la
clase Catálogo y producto ,realizar un objeto dentro de un catálogo productos el cual debe
tener un método para agregar productos y otra para mostrar toda la lista de productos.
"""
class Producto:
    def __init__(self,nombre,descripcion,precio):
        self.nombre=nombre
        self.descripcion=descripcion
        self.precio=precio
    def __str__(self):
        return f"{self.nombre} - {self.descripcion} - {self.precio}"
    
class Catalogo:
    def __init__(self):
        self.productos=["Bujias","Llantas"]
        
    def agregar_producto(self,producto):
        self.productos.append(producto)

    def mostrar_producto(self):
        for pr in self.productos:
            print(pr)