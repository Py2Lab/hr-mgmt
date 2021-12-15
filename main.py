import os


def menu():
    """
    Muestra el menu principal en la pantalla
    """
    print("Bienvenid@ a Py2Lab HR")
    print("Selecciona una opción")
    print("1. Consultar emplead@s")
    print("2. Agregar emplead@s")
    print("3. Modificar emplead@")
    print("4. Borrar emplead@")
    print("5. Salir")


while True:
    menu()

    opcion = input("Inserta una opción >> ")

    if opcion == "1":
        print("Has elegido la opcion 1")
        # Mandar a llamar la funcion de consultar empleados
    elif opcion == "2":
        print("Has elegido la opcion 2")
        # Mandar a llamar la funcion de argrgar empleados
    elif opcion == "3":
        print("Has elegido la opcion 3")
            print("por favor inserta el id del empleado")
                id = input
                    print("el empleado a modificar el el << id >>")
                        print("id")
        # Implementa el código para que se pida el id del empleado
        # Imprimir el mensaje de: Por favor inserta el id del empleado
        # identificador = 
        # Imprimir el mensaje de: El empleado a borrar es el << id >>
        # print(identificador)
    elif opcion == "4":
        print("Has elegido la opcion 4")
        # Implementa el código para que se pida el id del empleado
        # Imprimir el mensaje de: Por favor inserta el id del empleado
        # identificador = 
        # Imprimir el mensaje de: El empleado a borrar es el << id >>
        # print(identificador)
    elif opcion == "5":
        break
    else:
        print("No has elegido una opcion válida")