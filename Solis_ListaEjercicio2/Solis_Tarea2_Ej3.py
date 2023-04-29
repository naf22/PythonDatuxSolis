""""3. Definir una función que retorne el mayor valor al ingresar 2 números"""
valor1 =int(input("Ingrese el primer numero a comparar: "))
valor2 =int(input("Ingrese el segundo numero a comparar: "))
def maxvalor(valor1,valor2):
    if valor1>valor2:
        return valor1
    else:
        return valor2
    
print("El maximo valor es :  ",maxvalor(valor1,valor2))