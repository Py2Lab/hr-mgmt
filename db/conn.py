import mysql.connector

conn = mysql.connector.connect(user="jess", database="py2lab", password="12345")
cursor = conn.cursor()

def consulta_empleados():
    consulta = "SELECT * FROM empleado"
    cursor.execute(consulta)
    records = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    result = [dict(zip(column_names, record)) for record in records]
    return result

def consulta_empleado(empleado_id):
    consulta = f"SELECT * FROM empleado WHERE id={empleado_id}"

    cursor.execute(consulta)
    records = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    result = [dict(zip(column_names, record)) for record in records][0]
    return result

# TODO: Implementar la función de inserción de un nuevo empleado
# args: Los atributos del empleado
# return: Los datos del empleado {"id": id, "nombre": nombre ...}
def inserta_empleado():
    # Generar la consulta con los argumentos
    # Ejecutar la consulta
    # Traer los datos de la ejecución de la consulta (empleado creado)
    # Generar el diccionario con los datos del empleado para regresarlo
    pass

def actualiza_empleado():
    pass


def elimina_empleado(empleado_id):
    tablas_relacionadas = ["contacto", "direccion", "documento_empleado", "empresa_empleado"]

    for tabla in tablas_relacionadas:
        consulta_relacionada = construye_consulta_borrado(tabla, "empleado_id", empleado_id)
        realiza_consulta(consulta_relacionada)

    realiza_consulta(construye_consulta_borrado("empleado", "id", empleado_id))


# TODO: ¿Este es buen lugar para escribir estas funciones?
def construye_consulta_borrado(tabla, columna, valor_columna):
    consulta = f"DELETE FROM {tabla} WHERE {columna}={valor_columna}"
    return consulta

def realiza_consulta(consulta):
    cursor.execute(consulta)
    conn.commit()
