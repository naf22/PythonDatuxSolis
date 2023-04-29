""""4. Definir una función que imprima los argumentos ingresados desde línea de comandos
Nota: Usar import sys.argv => *args
"""
import sys

def imprimir_argumentos(*args):
    for arg in args:
        print(arg)
        
imprimir_argumentos(1,3,4,"hola")