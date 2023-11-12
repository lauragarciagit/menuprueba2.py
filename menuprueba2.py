import os
import json

def cargar_libros():
    try:
        with open('libros.json', 'r') as file:
            libros = json.load(file)
        return libros
    except FileNotFoundError:
        return []

def guardar_libros(libros):
    with open('libros.json', 'w') as file:
        json.dump(libros, file)

def menu():
    salir = False  # Variable to control the exit from the platform

    while not salir:
        print("""\n:::Bienvenidos a nuestra plataforma:::
        ¿Qué desea realizar?: 
        [1]- Entrar a la plataforma
        [2]- Salir de la plataforma\n""")

        option_str = input("Ingrese la opción deseada: ")
        try:
            option = int(option_str)
        except ValueError:
            print("Ingrese un número válido.")
            continue

        if option == 2:
            print("Ha salido de la plataforma. Hasta luego")
            salir = True  # Set the variable to True to exit the outer loop
        elif option == 1:
            print("Estamos en la plataforma")
            libros = cargar_libros()

            while True:
                print("""\nCómo desea seguir?: 
                [1]- Agregar un libro
                [2]- Ver listado de libros
                [3]- Modificar un libro
                [4]- Borrar un libro
                [5]- Salir a la plataforma\n""")

                search_option_str = input("Ingrese la opción de búsqueda: ")
                try:
                    search_option = int(search_option_str)
                except ValueError:
                    print("Ingrese un número válido.")
                    continue

                if search_option == 1:
                    titulo = input("Ingrese el título del libro: ")
                    libros.append({"titulo": titulo})
                    print("Ha agregado el libro:", titulo)
                    guardar_libros(libros)

                elif search_option == 2:
                    if not libros:
                        print("La lista de libros está vacía.")
                    else:
                        print("Listado de libros:")
                        for libro in libros:
                            print(libro['titulo'])

                elif search_option == 3:
                    titulo_modificar = input("¿Cuál libro desea modificar?: ")
                    nuevo_titulo = input("Ingrese el nuevo título: ")

                    for libro in libros:
                        if libro['titulo'] == titulo_modificar:
                            libro['titulo'] = nuevo_titulo
                            print("\nLibro modificado con éxito.")
                            guardar_libros(libros)
                            break
                    else:
                        print("\nLibro no encontrado.")

                elif search_option == 4:
                    titulo_borrar = input("¿Cuál libro desea borrar?: ")

                    for libro in libros:
                        if libro['titulo'] == titulo_borrar:
                            libros.remove(libro)
                            print("\nLibro eliminado con éxito.")
                            guardar_libros(libros)
                            break
                    else:
                        print("\nLibro no encontrado.")

                elif search_option == 5:
                    print("\nHa salido de la plataforma.")
                    salir = True  # Set the variable to True to exit both loops
                    break

                else:
                    print("Opción no válida. Seleccione una opción válida")

if __name__ == "__main__":
    if not os.path.exists('libros.json'):
        with open('libros.json', 'w') as file:
            file.write('[]')

    menu()