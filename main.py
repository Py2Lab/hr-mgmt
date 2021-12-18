import os


def imprime_datos_empleado(id, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, puesto, profesion, especialidad, dias_vacaciones, sueldo):

    print("Número de empleado: ", id)
    print("Nombre: ", nombre)
    print("Apellido paterno", apellido_paterno)
    print("Apellido materno", apellido_materno)
    print("Fecha de nacimiento", fecha_nacimiento)
    print("Puesto", puesto)
    print("Profesion", profesion)
    print("Especialidad", especialidad)
    print("Dias de vacaciones", dias_vacaciones)
    print("Sueldo", sueldo)

def imprime_cabecera(cabecera):
    """
    Imprime la cabecera entre asteriscos
    """
    print("**********************************")
    print(cabecera)
    print("**********************************")

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

        imprime_cabecera("Has elegido la opcion 1")

        # Mandar a llamar la funcion de consultar empleados
        opcion_consulta = input("¿Consultar empleado por ID o todos los empleados (Id|Todos)? >> ")
        if opcion_consulta == "Id":
            # Mostrar los datos del empleado con ese id
            id = input("Introduza el número de empleado a consultar >> ")
            # TODO: Implementar la consulta por empleado a la base de datos
            # SELECT * FROM employee WHERE id = id;

            nombre = "Pedro"
            apellido_paterno = "Moreno"
            apellido_materno = "Perez"
            fecha_nacimiento = "123456"
            puesto = "123456"
            profesion = "123456"
            especialidad = "123456"
            dias_vacaciones = "123456"
            sueldo = "123456"

            imprime_datos_empleado(id, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, puesto, profesion, especialidad, dias_vacaciones, sueldo)

        elif opcion_consulta == "Todos":
            print("Todos los empleados")
            # TODO: Implementar consulta a la base de datos
            # SELECT * FROM employee;
        else:
            print("Opción no válida")
    elif opcion == "2":

        imprime_cabecera("Has elegido la opcion 2")

        nombre = input("Introduce el nombre del empleado >> ")
        apellido_paterno = input("Introduce el apellido paterno >> ")
        apellido_materno = input("Introduce el apellido materno >> ")
        fecha_nacimiento = input("Introduce la fecha de nacimiento AAAA/MM/DD >> ")
        puesto = input("Introduce el puesto del empleado >> ")
        profesion = input("Introduce la profesion del empleado >> ")
        especialidad = input("Introduce la especialidad del empleado >> ")
        dias_vacaciones = input("Introduce los días de vacaciones >> ")
        sueldo = input("Introduce el sueldo del empleado >> ")

        
        imprime_cabecera("Los datos del empleado son: ")

        imprime_datos_empleado("-", nombre, apellido_paterno, apellido_materno, fecha_nacimiento, puesto, profesion, especialidad, dias_vacaciones, sueldo)
        print("********************************")
        correcto = input("¿Son correctos los datos del emplead@? (S/N) >> ")
        if correcto == "S":
            print("Empleado Guardado")
        elif correcto == "N":
            print("Empleado no Guardado")
        else:
            break
        print("********************************")
        # Mandar a llamar la funcion de argregar empleados
    elif opcion == "3":
        
        imprime_cabecera("Has elegido la opcion 3")

        id = input("Por favor inserta el id del empleado >> ")
        print("El número de empleado a modificar es el ", id)
        # Buscar al empleado en la base con el id -> SELECT * FROM employee WHERE id = id
        nombre = "123456"
        apellido_paterno = "123456"
        apellido_materno = "123456"
        fecha_nacimiento = "123456"
        puesto = "123456"
        profesion = "123456"
        especialidad = "123456"
        dias_vacaciones = "123456"
        sueldo = "123456"

        print("Los datos del empleado a modificar son: ")


        
        imprime_cabecera("Los datos del empleado son: ")
        
        imprime_datos_empleado(id, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, puesto, profesion, especialidad, dias_vacaciones, sueldo)
        print("********************************")

        while True:

            dato_modificar = input("¿Qué dato desea modificar? (Nombre|Paterno|Materno|Nacimiento|Puesto|Profesion|Especialdiad|Vacaciones|Sueldo) >> ")

            if dato_modificar == "Nombre":
                nombre = input("Introduzca el nuevo nombre >> ")
            elif dato_modificar == "Paterno":
                apellido_paterno = input("Introduzca el nuevo apellido paterno >> ")
            elif dato_modificar == "Materno":
                apellido_materno = input("Introduce el nuevo apellido materno >> ")
            elif dato_modificar == "Nacimiento":
                fecha_nacimiento = input("Introduce la nueva fecha de nacimiento >> ")
            elif dato_modificar == "Puesto":
                puesto = input("Introduce el nuevo puesto >> ")
            elif dato_modificar == "Profesion":
                profesion = input("Introduce la nueva profesion >> ")
            elif dato_modificar == "Especialidad":
                especialidad = input("Introduce la nueva especialidad >> ")
            elif dato_modificar == "Vacaciones":
                dias_vacaciones = input("Introduce los nuevos dias de vacaciones >> ")
            elif dato_modificar == "Sueldo":
                sueldo = input("Introduce el nuevo sueldo >> ")
            elif dato_modificar == "Terminar":
                # Implementar la edición del empleado en la base de datos
                # UPDATE employee set name = nombre, last_name=apellido_paterno WHERE id = id
                print("Emplead@ modificado exitosamente")
                break
            else:
                print("Opción no válida")
                break

            
            imprime_cabecera("Los datos modificados del empleado son: ")

            imprime_datos_empleado(id, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, puesto, profesion, especialidad, dias_vacaciones, sueldo)
            print("********************************")

    elif opcion == "4":

        imprime_cabecera("Has elegido la opcion 4")
        
        id = input("Por favor inserta el id del empleado >> ")
        print("El número de empleado a eliminar es el ", id)
        # Implementa el código para que se pida el id del empleado
        # Imprimir el mensaje de: Por favor inserta el id del empleado
        # identificador = 
        # Imprimir el mensaje de: El empleado a borrar es el << id >>
        # print(identificador)
    elif opcion == "5":

        imprime_cabecera("¡Adiós, vaquer@!")
        
        break
    else:
        print("No has elegido una opcion válida")