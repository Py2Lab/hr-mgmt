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
        print("********************************")
        print("Has elegido la opcion 2")
        print("********************************")
        nombre = input("Introduce el nombre del empleado >> ")
        apellido_paterno = input("Introduce el apellido paterno >> ")
        apellido_materno = input("Introduce el apellido materno >> ")
        fecha_nacimiento = input("Introduce la fecha de nacimiento AAAA/MM/DD >> ")
        puesto = input("Introduce el puesto del empleado >> ")
        profesion = input("Introduce la profesion del empleado >> ")
        especialidad = input("Introduce la especialidad del empleado >> ")
        dias_vacaciones = input("Introduce los días de vacaciones >> ")
        sueldo = input("Introduce el sueldo del empleado >> ")

        print("********************************")
        print("Los datos del empleado son: ")
        print("********************************")
        print("Nombre: ", nombre)
        print("Apellido Paterno: ", apellido_paterno)
        print("Apellido Materno", apellido_materno)
        print("Fecha de Nacimiento: ", fecha_nacimiento)
        print("Puesto: ", puesto)
        print("Profesion: ", profesion)
        print("Especialidad: ", especialidad)
        print("Días de vacaciones: ", dias_vacaciones)
        print("Sueldo: ", sueldo)
        print("********************************")
        correcto = input("¿Son correctos los datos del emplead@? (S/N)")
        if correcto == "S":
            print("Empleado Guardado")
        elif correcto == "N":
            print("Empleado no Guardado")
        else:
            break
        print("********************************")
        # Mandar a llamar la funcion de argregar empleados
    elif opcion == "3":
        print("Has elegido la opcion 3")
        id = input("por favor inserta el id del empleado >> ")
        print("el numero de empleado a modificar es el ", id)
        # Implementa el código para que se pida el id del empleado
        # Imprimir el mensaje de: Por favor inserta el id del empleado
        # identificador = 
        # Imprimir el mensaje de: El empleado a borrar es el << id >>
        # print(identificador)
    elif opcion == "4":
        print("Has elegido la opcion 4")
        id = input("por favor inserta el id del empleado >> ")
        print("el numero de empleado a eliminar es el ", id)
        # Implementa el código para que se pida el id del empleado
        # Imprimir el mensaje de: Por favor inserta el id del empleado
        # identificador = 
        # Imprimir el mensaje de: El empleado a borrar es el << id >>
        # print(identificador)
    elif opcion == "5":
        break
    else:
        print("No has elegido una opcion válida")