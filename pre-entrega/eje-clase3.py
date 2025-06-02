"""
Solicite al cliente o clienta su nombre, apellido, edad y correo electrónico.
Compruebe que el nombre, el apellido y el correo no estén en blanco, y que la edad sea mayor a 18 años.
Muestre los datos por la terminal, en el orden que se ingresaron. Si alguno de los datos ingresados no cumple los requisitos, sólo mostrar el texto “ERROR!”.
"""
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
correo = input("Ingrese su correo electrónico: ")
if nombre and apellido and correo and edad.isdigit() and int(edad) > 18:
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Edad:", edad)
    print("Correo electrónico:", correo)
else:
    print("ERROR!")