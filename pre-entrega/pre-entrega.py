"""
Ingreso de datos de productos: El sistema debe permitir ingresar datos básicos de los productos: nombre, categoría, y precio (sin centavos). Estos datos deben almacenarse en una lista, donde cada cliente sea representado/a como una sublista de tres elementos (nombre, categoría, y precio).
Visualización de productos registrados: El programa debe incluir una funcionalidad para mostrar en pantalla todos los productos ingresados. La información debe presentarse de manera ordenada y legible, con cada producto numerado.
Búsqueda de productos: El sistema debe permitir buscar productos por su nombre. Si encuentra coincidencias, debe mostrar la información completa de los productos que coincidan. Si no hay coincidencias, debe informar que no se encontraron resultados.
Eliminación de productos: El sistema debe permitir eliminar un producto de la lista, identificándolo por su posición (número) en la lista.
Requisitos
Usar listas para almacenar y gestionar los datos. 
Incorporar bucles while y for según corresponda. 
Validar entradas del usuario o usuaria, asegurándote de que no se ingresen datos vacíos o incorrectos.
Utilizar condicionales para gestionar las opciones del menú y las validaciones necesarias.
Presentar un menú que permita elegir entre las funcionalidades disponibles: agregar productos, visualizar productos, buscar productos y eliminar productos.
El programa debe continuar funcionando hasta que se elija una opción para salir.
Ejemplo del menú de opciones:
Sistema de Gestión Básica De Productos:
1. Agregar producto
2. Mostrar productos
3. Buscar producto
4. Eliminar producto
5. Salir
"""

productos = []
while True:
    print("\nSistema de Gestión Básica De Productos:")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ").strip()
    
    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del producto: ").strip()
            categoria = input("Ingrese la categoría del producto: ").strip()
            precio = input("Ingrese el precio del producto (sin centavos): ").strip()

            if nombre and categoria and precio.isdigit():
                productos.append([nombre, categoria, int(precio)])
                print("Producto agregado exitosamente.")
            else:
                print("ERROR! Todos los campos son obligatorios y el precio debe ser un número.")
        case "2":
            if productos:
                print("Productos registrados:")
                for i, producto in enumerate(productos, start=1):
                    print(f"{i}. Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: {producto[2]}")
            else:
                print("No hay productos registrados.")
        case "3":
            if productos:
                nombre_buscar = input("Ingrese el nombre (o parte) del producto a buscar: ").strip()
                encontrados = []
                for producto in productos:
                    if nombre_buscar.lower() in producto[0].lower():
                        encontrados.append(producto)
                
                if encontrados:
                    print("Productos encontrados:")
                    for i, producto in enumerate(encontrados, start=1):
                        print(f"{i}. Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: {producto[2]}")
                else:
                    print("No se encontraron productos con ese nombre.")
            else:
                print("No hay productos registrados.")
        case "4":
            if productos:
                print("Productos registrados:")
                for i, producto in enumerate(productos, start=1):
                    print(f"{i}. Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: {producto[2]}")
                
                posicion = int(input("Ingrese el número del producto a eliminar: ")) - 1
                if 0 <= posicion < len(productos):
                    productos.pop(posicion)
                    print("Producto eliminado exitosamente.")
                else:
                    print("ERROR! Número de producto inválido.")
            else:
                print("No hay productos registrados.")
        case "5":
            print("Saliendo del sistema...")
            break
        case _:
            print("ERROR! Opción inválida.")

