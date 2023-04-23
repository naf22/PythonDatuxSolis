""""6.Realice un programa que calcule la suma de los números hasta el valor ingresado.
Ejemplo : si se ingresa 5 se tendrá que calcular 1+2+3+4+5."""

valor_referencia=int(input("Ingrese el valor limite de la suma : "))
suma=0
for i in range(1,valor_referencia+1):
   suma =suma+ i
print("la suma final es : " +str(suma))


""""Tambien se puede realizar mediante el uso de la formula: valor_Referencia(valor_referencia +1 )/2 """