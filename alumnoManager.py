class AlumnoManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def alta_alumno(self, ci, nombre, apellido, fecha_nacimiento, telefono, correo_electronico):
        try:
            cursor = self.db_connection.cursor()
            query = """
                INSERT INTO alumnos (ci, nombre, apellido, fecha_nacimiento, telefono, correo_electronico)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (ci, nombre, apellido, fecha_nacimiento, telefono, correo_electronico))
            self.db_connection.commit()
            print("Alumno agregado exitosamente")
        except Exception as e:
            print(f"Error al agregar alumno: {e}")
            self.db_connection.rollback()

    def baja_alumno(self, ci):
        try:
            cursor = self.db_connection.cursor()
            query = "DELETE FROM alumnos WHERE ci = %s"
            cursor.execute(query, (ci,))
            self.db_connection.commit()
            print("Alumno eliminado exitosamente")
        except Exception as e:
            print(f"Error al eliminar alumno: {e}")
            self.db_connection.rollback()

    def modificar_alumno(self, ci, nombre=None, apellido=None, fecha_nacimiento=None, telefono=None, correo_electronico=None):
        try:
            cursor = self.db_connection.cursor()
            query = "UPDATE alumnos SET "
            params = []
            if nombre:
                query += "nombre = %s, "
                params.append(nombre)
            if apellido:
                query += "apellido = %s, "
                params.append(apellido)
            if fecha_nacimiento:
                query += "fecha_nacimiento = %s, "
                params.append(fecha_nacimiento)
            if telefono:
                query += "telefono = %s, "
                params.append(telefono)
            if correo_electronico:
                query += "correo_electronico = %s, "
                params.append(correo_electronico)

            query = query.rstrip(", ")  # Eliminar la última coma y espacio
            query += " WHERE ci = %s"
            params.append(ci)

            cursor.execute(query, tuple(params))
            self.db_connection.commit()
            print("Alumno modificado exitosamente")
        except Exception as e:
            print(f"Error al modificar alumno: {e}")
            self.db_connection.rollback()

    def obtener_alumno(self, ci):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM alumnos WHERE ci = %s"
            cursor.execute(query, (ci,))
            alumno = cursor.fetchone()
            if alumno:
                return alumno
            else:
                print("Alumno no encontrado")
        except Exception as e:
            print(f"Error al obtener alumno: {e}")