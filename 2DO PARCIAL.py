
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="tareas_db"
)

cursor = db.cursor()
create_table_query = """
CREATE TABLE IF NOT EXISTS tareas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255) NOT NULL,
    fecha_creacion DATE NOT NULL,
    completada BOOLEAN NOT NULL
)
"""

cursor.execute(create_table_query)
db.commit()
from datetime import date

def agregar_tarea(descripcion):
    fecha_creacion = date.today()
    completada = False

    insert_query = """
    INSERT INTO tareas (descripcion, fecha_creacion, completada)
    VALUES (%s, %s, %s)
    """

    cursor.execute(insert_query, (descripcion, fecha_creacion, completada))
    db.commit()

def marcar_completada(id_tarea):
    update_query = """
    UPDATE tareas
    SET completada = TRUE
    WHERE id = %s
    """

    cursor.execute(update_query, (id_tarea,))
    db.commit()

def listar_tareas_pendientes():
    select_query = """
    SELECT * FROM tareas
    WHERE completada = FALSE
    """

    cursor.execute(select_query)
    result = cursor.fetchall()

    return result

def eliminar_tarea(id_tarea):
    delete_query = """
    DELETE FROM tareas
    WHERE id = %s
    """

    cursor.execute(delete_query, (id_tarea,))
    db.commit()
if __name__ == "__main__":
    while True:
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Listar tareas pendientes")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            agregar_tarea(descripcion)
        elif opcion == "2":
            id_tarea = input("Ingrese el ID de la tarea a marcar como completada: ")
            marcar_completada(id_tarea)
        elif opcion == "3":
            tareas_pendientes = listar_tareas_pendientes()
            for tarea in tareas_pendientes:
                print(f"ID: {tarea[0]}, Descripción: {tarea[1]}, Fecha de Creación: {tarea[2]}, Completada: {tarea[3]}")
        elif opcion == "4":
            id_tarea = input("Ingrese el ID de la tarea a eliminar: ")
            eliminar_tarea(id_tarea)
        elif opcion == "5":
            break
