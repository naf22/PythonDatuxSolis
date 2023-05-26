import lib.Prueba.Ejercicio2 as p2
import lib.Prueba.Ejercicio3 as p3
import lib.Prueba.Ejercicio4 as p4
import lib.Prueba.Ejercicio5 as p5
import lib.Prueba.Ejercicio6 as p6
import lib.Prueba.Ejercicio7 as p7
if __name__=='__main__':
    while(True):
        opcion=input("""Elija que ejercicio de la tarea del modulo 3 quiere ejecutar \n
        2.Ejecicio 2 \n
        3.Ejecicio 3 \n
        4.Ejecicio 4 \n
        5.Ejecicio 5 \n
        6.Ejecicio 6 \n
        7.Ejecicio 7 \n
        8.Salir: """)
        if opcion=="2":
            print("---------------------------------------------------")
            print(" Se esta ejecutando el Ejercicio 2")
            producto=input("Ingresa el producto a agregar : ")
            e2 =p2.Catalogo()
            e2.agregar_producto(producto)
            print("----------Lista de Productos----------")
            e2.mostrar_producto()
        elif opcion=="3":
            print("---------------------------------------------------")
            print(" Se esta ejecutando el Ejercicio 3")
            p3.Menu_iterativo_ej3()
        elif opcion=="4":
            print("---------------------------------------------------")
            print(" Se esta ejecutando el Ejercicio 4")
            e4=p4.Producto("Escritorio", "PERU-0001-2023")
            e5=p4.Producto("Cuaderno", "ARGENTINA-0002-2023")
            print("Permitira identificar el pais,lote y año  de los 2 registros que cree")
            print("REGISTRO 1:")
            print(e4)
            print("REGISTRO 2:")
            print(e5)
        elif opcion=="5":
            print("---------------------------------------------------")
            print(" Se esta ejecutando el Ejercicio 5")
            e5=p5.Producto("Escritorio", "PERU-0001-2023")
            e6=p5.Producto("Cuaderno", "ARGENTINA00022023")
            print("ESTE CODIGO PERMITIRA VERIFICAR SI LOS DOS REGISTRADOS INGRESADOS SON CORRECTOS")
            print("REGISTRO 1:")
            print(e5)
            print("REGISTRO 2:")
            print(e6)
        elif opcion=="6":
            print("---------------------------------------------------")
            peli1=p6.Pelicula("Hombre Araña x",120,2020,"terror")
            peli2=p6.Pelicula("Liga de la justicia",80,2023,"accion")
            e6_1=p6.Catalogo()
            e6_1.agregar(peli1)
            e6_1.agregar(peli2)
            print(" Se esta ejecutando el Ejercicio 6")
            Año=int(input("Ingresa el año que quiere filtrar : "))
            Resu1=e6_1.FiltroAñosSolis(Año)
            print(Resu1)
            Genero=input("Ingresa el genero que quiere filtrar,(solo hay registro con terror y accion): ")
            Resu2=e6_1.FiltroGeneroSolis(Genero)
            print(Resu2)
        elif opcion=="7":
            print("---------------------------------------------------")
            print(" Se esta ejecutando el Ejercicio 7")
            nombre=input("Ingresa el nombre(atribuo de la clase Persona): ")
            apellido=input("Ingresa el apellido(atribuo de la clase Persona): ")
            edad=input("Ingresa la edad(atribuo de la clase Persona): ")
            o7=p7.Persona(nombre,apellido,edad)
            print("Se creo existosamente un objeto de la clase Persona")
        elif opcion=="8":
            print("----------GRACIAS POR USAR EL MENU DE LA TAREA 3_SOLIS----------")
            break           

            
            
