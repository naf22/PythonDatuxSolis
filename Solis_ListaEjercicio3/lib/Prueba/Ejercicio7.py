class Persona:
    def __init__(self,nombre,apellido,edad) -> None:
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    def __str__(self) -> str:
        return f"Nombres: {self.nombre} Apellidos: {self.apellido}  y tiene una edad: {self.edad} "
    

