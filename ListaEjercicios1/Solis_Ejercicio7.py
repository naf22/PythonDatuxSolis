""""Ejercicio 7. Realiza un programa que lea 2 números por teclado y determine los siguientes
aspectos:
● Si los dos números son iguales
● Si los dos números son diferentes
● Si el primero es mayor que el segundo
● Si el segundo es mayor o igual que el primero
"""
valor1 =input("Ingrese el pimer valor: ")
valor2 =input("Ingrese el segundo valor: ")
if valor1==valor2 :
    print("Los dos numeros son iguales")
else :
    print("Los dos numeros son diferentes")
    if valor1>valor2:
        print("El primer numero  es el mayor")
    else :
        print("El segundo numero es el mayor")