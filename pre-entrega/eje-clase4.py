"""
Solicite al cliente o clienta su nombre, apellido, edad y correo electrónico.
Compruebe que el nombre, el apellido y el correo no estén en blanco, y que la edad sea mayor a 18 años.
Muestre los datos por la terminal, en el orden que se ingresaron. Si alguno de los datos ingresados no cumple los requisitos, sólo mostrar el texto “ERROR!”.
Formatee correctamente los textos ingresados en “apellido” y “nombre”, convirtiendo la primera letra de cada palabra a mayúsculas y el resto en minúsculas.
Asegurarse que el correo electrónico no tenga espacios y contenga solo una “@”.
Que clasifique por rango etario basándose en su edad (“Niño/a” para los menores de 15 años, “Adolescente” de 15 a 18 y “Adulto/a” para los mayores de 18 años.)
"""
nombre = input("Ingrese su nombre: ").strip()
apellido = input("Ingrese su apellido: ").strip()
edad = input("Ingrese su edad: ")
correo = input("Ingrese su correo electrónico: ").strip()
if nombre and apellido and correo and edad.isdigit() and int(edad) > 18:
    nombre = nombre.title()
    apellido = apellido.title()
    correo = correo
    if "@" in correo and correo.count("@") == 1:
        if int(edad) < 15:
            rango_etario = "Niño/a"
        elif 15 <= int(edad) <= 18:
            rango_etario = "Adolescente"
        else:
            rango_etario = "Adulto/a"
        print("Nombre:", nombre)
        print("Apellido:", apellido)
        print("Edad:", edad)
        print("Correo electrónico:", correo)
        print("Rango etario:", rango_etario)
    else:
        print("ERROR!")