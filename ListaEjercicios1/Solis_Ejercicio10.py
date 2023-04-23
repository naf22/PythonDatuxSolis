""""10. Defina una lista de DNI’s y otra lista de datos que tenga lista anidadas en donde
si la posición del DNI es x la información se encuentra en la posición x de la lista de
datos, pedir datos para validar si el usuario tiene permitido ingresar , validar que
exista en la lista de dni , que su edad sea mayor a 18 años y que sea datux en el
curso de python.
Ejemplo : [ ‘name’, edad,’distrito’,’datux’,’curso:sql’]"""

dni_list = [12345678, 23456789, 34567890, 45678901]
data_list = [['Juan', 20, 'SJL', 'datux', 'curso:python'], 
             ['Maria', 25, 'MOLINA', 'no_datux', 'curso:python'], 
             ['Pedro', 30, 'VMT', 'datux', 'curso:sql'], 
             ['Lucia', 19, 'CL', 'datux', 'curso:python']]

dni = int(input("Ingrese su DNI: "))
edad = int(input("Ingrese su edad: "))

if dni in dni_list and edad > 18:
    index = dni_list.index(dni)
    user_data = data_list[index]
    if user_data[3] == 'datux' and user_data[4]== 'curso:python':
        print("El usuario puede ingresar.")
    else:
        print("El usuario no tiene permitido ingresar.")
else:
    print("El usuario no tiene permitido ingresar.")