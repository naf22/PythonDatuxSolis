"""3. validar una entrada mediante una expresión regular (numérica , texto , email ,celular etc)
"""
import re
def validar_numero(entrada):
    patron = r'^\d+$'
    if re.match(patron, entrada):
        print("La entrada es un número válido.")
    else:
        print("La entrada no es un número válido.")

def validar_texto(entrada):
    patron = r'^[a-zA-Z\s]+$'  
    if re.match(patron, entrada):
        print("La entrada es un texto válido.")
    else:
        print("La entrada no es un texto válido.")

def validar_email(enail):
    patron = r'[a-zA-Z0-9_.+-]+@gmail\.com$'
    if re.match(patron, enail):
        print("La entrada es un email válido.")
    else:
        print("La entrada no es un email válido.")


print("----Este es un ejemplo de validacion de un dato numerico----")
validar_numero("12345")
validar_numero("ASASDASD")
print("----Este es un ejemplo de validacion de un dato tipo texto----")
validar_texto("Hola Mundo")
validar_texto("32423432")
print("----Este es un ejemplo de validacion de un dato tipo email----")
validar_email("moisesSolis@gmail.com")
validar_email("moisesSolis2232.com")