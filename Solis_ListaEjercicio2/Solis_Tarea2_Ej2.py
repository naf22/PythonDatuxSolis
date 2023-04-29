""""2.Realizar un Programa que simule funcionalidades de una Biblioteca, definir la biblioteca
como un diccionario.
2.1 La biblioteca deberá tener las siguientes operaciones:
- Obtener la lista de categorías de libros.
-Obtener nombres de los libros y autores.
-poder cambiar el estado de un libro a prestado
-Lista de usuarios de la biblioteca.
"""
Biblioteca_Solis={
    "Categorias":["Ciencia Ficcion","Literatura","Novela","Biografias"],
    "Libros":{
        "Cien años de soledad":{
            "autor":"Gabriel Garcia Marquez",
            "estado":"Disponible"
        },
        "La Odisea":{
            "autor":"Homero",
            "estado":"Disponible"
        },
        "Venas Abiertas de America Latina":{
            "autor":"Eduardo Galeani",
            "estado":"prestado"
        }
    },
    "usuarios":["juanca","marcelo","rosy","antonio"]
}
while True :
    print("--------------Tarea 2--------------")
    opcion =input("""Eliga la opcion : \n
    1.Obtener lista de categorias de libros: \n
    2.Obtener nombres de los libros y autores: \n
    3.Cambiar el estado de un libro: \n
    4.Listar usuarios de la biblioteca: \n
    5.Salir: 
      """)
    if opcion=="1":
        print("----------------------------")
        categorias =Biblioteca_Solis["Categorias"]
        print("Las categorias son: ", categorias)
    elif opcion=="2":
        print("----------------------------")
        libros= Biblioteca_Solis["Libros"]
        for titulo,datos in libros.items():
            autor=datos["autor"]
            print("Titulo: \n",titulo,"\n","Autor: \n",autor)
            print("----------------------------")
    elif opcion=="3":
        opLibro=input("""Escoja el libro que quiera pasar a estado de Prestado: \n
                      1.Cien años de soledad \n
                      2.La Odisea \n
                      3.Venas Abiertas de America Latina """)
        libros2= Biblioteca_Solis["Libros"]
        if opLibro=="1" :
            libros2["Cien años de soledad"][1]="prestado"
            print(libros2.keys(),"\n",libros2.values())
        elif opLibro=="2" :
            libros2["La Odisea"][1]="prestado"
            print(libros2.keys(),"\n",libros2.values())
        elif opLibro=="3" :
            libros2["Venas Abiertas de America Latina"][1]="prestado"
            print(libros2.keys(),"\n",libros2.values())
        else :
            "No existe tal libro"
    elif opcion=="4":
        print("----------------------------")
        usuarios =Biblioteca_Solis["usuarios"]
        print("Los usuarios son: ", usuarios)

    elif opcion=="5":
        print("Gracias por utilizar el menu")
        print("----------------------------")
        break

