class ClaseManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def agregar_clase(self, ci_instructor, id_actividad, id_turno):
        """
        Agrega una nueva clase al sistema.
        """
        try:
            cursor = self.db_connection.cursor()
            query = """
                INSERT INTO clase (ci_instructor, id_actividad, id_turno)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (ci_instructor, id_actividad, id_turno))
            self.db_connection.commit()
            print("Clase agregada exitosamente.")
        except Exception as e:
            print(f"Error al agregar la clase: {e}")
            self.db_connection.rollback()

    def modificar_clase(self, id_clase, ci_instructor=None, id_actividad=None, id_turno=None, dictada=None):
        """
        Modifica una clase existente en el sistema.
        """
        try:
            cursor = self.db_connection.cursor()
            query = "UPDATE clase SET "
            params = []
            
            if ci_instructor:
                query += "ci_instructor = %s, "
                params.append(ci_instructor)
            if id_actividad:
                query += "id_actividad = %s, "
                params.append(id_actividad)
            if id_turno:
                query += "id_turno = %s, "
                params.append(id_turno)
            if dictada is not None:
                query += "dictada = %s, "
                params.append(dictada)

            # Remover la última coma y espacio
            query = query.rstrip(", ")
            query += " WHERE id = %s"
            params.append(id_clase)

            cursor.execute(query, tuple(params))
            self.db_connection.commit()
            print("Clase modificada exitosamente.")
        except Exception as e:
            print(f"Error al modificar la clase: {e}")
            self.db_connection.rollback()

    def eliminar_clase(self, id_clase):
        """
        Elimina una clase por su ID.
        """
        try:
            cursor = self.db_connection.cursor()
            query = "DELETE FROM clase WHERE id = %s"
            cursor.execute(query, (id_clase,))
            self.db_connection.commit()
            print("Clase eliminada exitosamente.")
        except Exception as e:
            print(f"Error al eliminar la clase: {e}")
            self.db_connection.rollback()

    def listar_clases(self):
        """
        Lista todas las clases.
        """
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            query = """
                SELECT c.id, c.ci_instructor, i.nombre AS instructor_nombre, 
                       a.descripcion AS actividad, t.hora_inicio, t.hora_fin, c.dictada
                FROM clase c
                JOIN instructores i ON c.ci_instructor = i.ci
                JOIN actividades a ON c.id_actividad = a.id
                JOIN turnos t ON c.id_turno = t.id
                ORDER BY c.id
            """
            cursor.execute(query)
            clases = cursor.fetchall()
            for clase in clases:
                print(f"ID: {clase['id']}, Instructor: {clase['instructor_nombre']} "
                      f"({clase['ci_instructor']}), Actividad: {clase['actividad']}, "
                      f"Turno: {clase['hora_inicio']} - {clase['hora_fin']}, Dictada: {clase['dictada']}")
        except Exception as e:
            print(f"Error al listar clases: {e}")