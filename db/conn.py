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

def inserta_empleado():
    pass

def actualiza_empleado():
    pass

def elimina_empleado(empleado_id):
    # TODO: Implementar funcion
    consulta = "DELETE FROM empleado WHERE id={empleado_id}"
    cursor.execute(consulta)

