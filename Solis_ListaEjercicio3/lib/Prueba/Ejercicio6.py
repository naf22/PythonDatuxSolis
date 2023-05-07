class Pelicula:
    def __init__(self,titulo,duracion,release,genero) -> None:
        self.titulo=titulo
        self.release=release
        self.genero=genero
        self.duracion=duracion
    def __str__(self) -> str:
        return f"{self.titulo} se estreno el {self.release}  del genero {self.genero} y dura {self.duracion} minutos"

class Catalogo:
    listaPeliculas=[]
    def __init__(self) -> None:
        self.name="Catalogo Peliculas"
        self.listaPeliculas=[]
    def agregar(self, x):  # p será un objeto Pelicula
        self.listaPeliculas.append(x)
    def mostrar(self):
        for iterador in self.listaPeliculas:
            print(iterador)  # Print toma por defecto str(p)}  
    def filtroDuracion(self,duracion=0):
        resultadoFiltro=[]
        for iteradorPelicula in self.listaPeliculas:
            if iteradorPelicula.duracion>duracion:
                resultadoFiltro.append(iteradorPelicula)
        return resultadoFiltro      
 ## añadir filtro de release segun un año espeficio,FUNCIONALIDAD1
    def FiltroAñosSolis(self,año):
        try:
            resultadoFiltroAño=[]
            for iteradorPelicula in self.listaPeliculas:
                if iteradorPelicula.release==año:
                    listprueba=[iteradorPelicula.titulo,iteradorPelicula.release,iteradorPelicula.genero,iteradorPelicula.duracion]
                    resultadoFiltroAño.append(listprueba)
            return resultadoFiltroAño
        except:
         print("hubo un error")     
        
 #FUNCIONALIDAD 2
    def FiltroGeneroSolis(self,genero):
        resultadoFiltroGenero=[]
        for iteradorPelicula in self.listaPeliculas:
            if str(iteradorPelicula.genero)==genero:
                listprueba=[iteradorPelicula.titulo,iteradorPelicula.release,iteradorPelicula.genero,iteradorPelicula.duracion]
                resultadoFiltroGenero.append(listprueba)
        return resultadoFiltroGenero 

peli1=Pelicula("ant man",120,2020,"terror")
peli2=Pelicula("mario b",80,2023,"accion")
c1=Catalogo()
c1.agregar(peli1)
c1.agregar(peli2)
c1.mostrar()


