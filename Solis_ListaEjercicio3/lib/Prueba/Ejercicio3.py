import lib.Prueba.dvidir_ejercio3 as div_e3
def Menu_iterativo_ej3():
    while(True):
        opcion=input("""Elija la opcion :\n
        1.Dividir \n
        2.Salir: """)
        if opcion=="1":
            num1=int(input("Ingrese el primer valor: "))
            num2=int(input("Ingrese el segundo valor: "))
            div_e3.dividir_E3(num1,num2)
        else:
            print("Gracias por utilizar el menu iterativo del ejercio3")
            break

