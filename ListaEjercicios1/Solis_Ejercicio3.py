"""" Ejercicio 3.Ingrese 3 valores y realice las operaciones de suma ,resta ,multiplicación, división
y división entera.
"""
print("Lista de Operaciones de la calculadora : \n 1.Sumar \n 2.Restar \n 3.Multiplicar \n 4.División \n 5.División Entera ")
operacion=input("ingrese su operacion :  ")
numero1=float(input("Ingrese un numero: "))
numero2=float(input("Ingrese un numero: "))
if operacion=="1":
  print("El resultado de la suma es : "+ str(numero1+numero2))
elif operacion=="2":
 print("El resultado de la resta es : "+str(numero1-numero2))
elif operacion=="3":
 print("El resultado de la multiplicación es : "+ str(numero1*numero2))
elif operacion=="4":
 print("El resultado de la división es : " + str(numero1/numero2))
elif operacion=="5":
 print("El resultado de la división entera es : " + str(numero1//numero2))
else :
  print("no existe tal operación")