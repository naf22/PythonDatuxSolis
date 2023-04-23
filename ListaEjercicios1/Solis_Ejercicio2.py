"""Ejercicio2.Calcule el área de un círculo, triángulo y cuadrado con radio ingresado desde el
teclado"""

print("La calculadora contara con las siguientes opciones : \n 1.Calcular Area de un circulo \n 2.Calcular el area de un triangulo \n 3.Calcular el area de un Cuadrado")
print("-----------------------------------")
operacion=float(input("Ingrese el numero de operacion a realizar :  "))
if operacion==1:
    print("-----Hallando el area de un circulo------")
    radio=float(input("Ingrese el valor del radio:"))
    pi=3.1416
    area_circulo=pi*radio**2
    print("El area del circulo es "+str(area_circulo))
elif operacion==2:
     print("-----Hallando el area de un Triangulo------")
     base =float(input("Ingrese el valor de la base:"))
     altura =float(input("Ingrese el valor de la altura:"))
     print("EL area del triangulo es : "+str((base*altura)/2))
elif operacion==3:
    print("-----Hallando el area de un Cuadrado------")
    lado=float(input("Ingrese el valor del lado:"))
    print("EL area del Cuadrado es : "+str(lado**2))
else :
    print("No existe tal operación")