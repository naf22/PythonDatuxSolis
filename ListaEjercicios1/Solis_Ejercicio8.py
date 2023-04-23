""""8.Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la
contraseña introducida por el usuario coincide con la guardada en la variable sin
tener en cuenta mayúsculas y minúsculas."""

passw_guardada=input("Ingrese su contraseña: ")
print("----------------------------------------")
passw_2=input("Confirme su contraseña : ")
if passw_guardada.upper()==passw_2.upper() :
    print("Las contraseñas si son iguales")
else :
    print("Las contraseñas no son iguales")