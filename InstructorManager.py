# Clase para manejar instructores
class InstructorManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def agregar_instructor(self, ci, nombre, apellido):
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO instructores (ci, nombre, apellido) VALUES (%s, %s, %s)", (ci, nombre, apellido))
        self.db_connection.commit()
        print("Instructor agregado con éxito.")

    def eliminar_instructor(self, ci):
        cursor = self.db_connection.cursor()
        cursor.execute("DELETE FROM instructores WHERE ci = %s", (ci,))
        self.db_connection.commit()
        print("Instructor eliminado con éxito.")

    def modificar_instructor(self, ci, nombre=None, apellido=None):
        cursor = self.db_connection.cursor()
        if nombre:
            cursor.execute("UPDATE instructores SET nombre = %s WHERE ci = %s", (nombre, ci))
        if apellido:
            cursor.execute("UPDATE instructores SET apellido = %s WHERE ci = %s", (apellido, ci))
        self.db_connection.commit()
        print("Instructor modificado con éxito.")