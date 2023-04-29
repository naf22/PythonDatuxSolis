""""1.Realizar un Menú Iterativo que tenga las siguientes opciones(Solo poner el número de la
pregunta):
- Realizar un programa que dibuje un cuadrado en consola con *, usando bucles.
- Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e
imprimir el número
- Iterar una lista de elementos que contengan nombre y edad e imprimir solo los
mayores de edad.
Nota : cada elemento de la lista puede ser otra lista [[nombre,edad],.... ]"""


print("--------------------Menu Iterativo_Solis--------------------")
#lista de la opcion 2
lista_o2=[10,23,12,34,23,52,65,42,62]
#lista de la opcion 3
lista_o3=[['juanca',17],['Marcelo',23],['Antonio',22],['Rosy',16],['Moises',24],['Karla' ,32],['Shanice',16]]

while True :
    opcion=input("""Puede elegir las siguientes opciones:\n 
    1.Realizar un cuadrado con un bucle\n 
    2.Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e imprimir el número \n 
    3.Iterar una lista de elementos que contengan nombre y edad e imprimir solo los mayores de edad \n
    4.Salir: """)
    
    if opcion =="1" :
        print("----------------------------------------------")
        tamaño_lado=int(input("Ingrese la medida de un lado del cuadrado: "))
        for i in range(tamaño_lado) :
            print("*"*tamaño_lado)
    elif opcion=="2" :
        print("----------------------------------------------")
        for k,v in enumerate(lista_o2):
            if v%2==0 :
                print(str(v))
    elif opcion=="3":
        print("----------------------------------------------")
        for llave,valor in enumerate(lista_o3):
          if valor[1]>=18 :
              print(valor[0])
    elif opcion=="4":
        print("----------------------------------------------")
        print("Gracias por usar el menu")
        break
        
    else :
        print("----------------------------------------------")
        print("Comando no conocido")
     

