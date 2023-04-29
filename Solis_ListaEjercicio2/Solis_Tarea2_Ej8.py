""""8.Genear una funcion rango hasta un numero maximo (10^5), con un step y agregar a una lista
los números que cumplan las siguientes opciones , que sean primos"""

"setp = pasos o saltos"
primos =  list()
def Listar_primos(max_numero, pasos):
  
    for numero in range(2, max_numero + 1, pasos):
        for i in range(2, int(numero**(1/2)) + 1):
            if numero % i == 0:
                break
        else:
            primos.append(numero)
    return primos


Listar_primos(10**5,1)
print("--------------------------------------------------------------------------------------")
print("Como ejemplos mostraremos los primeros 100 numeros primos")
print(primos[:100])