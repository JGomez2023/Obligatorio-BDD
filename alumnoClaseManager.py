import mysql.connector

class AlumnoClaseManager:
    def __init__(self, conexion):
        self.conexion = conexion

    def inscribir_alumno(self, id_clase, ci_alumno, id_equipamiento=None):
        """
        Inscribir un alumno en una clase, opcionalmente con un equipamiento.
        """
        try:
            cursor = self.conexion.cursor()
            query = """
                INSERT INTO alumno_clase (id_clase, ci_alumno, id_equipamiento)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (id_clase, ci_alumno, id_equipamiento))
            self.conexion.commit()
            print(f"Alumno {ci_alumno} inscrito en la clase {id_clase}.")
        except mysql.connector.Error as e:
            print(f"Error al inscribir alumno: {e}")
        finally:
            cursor.close()

    def modificar_inscripcion(self, id_clase, ci_alumno, nuevo_id_equipamiento=None):
        """
        Modificar la inscripción de un alumno en una clase.
        """
        try:
            cursor = self.conexion.cursor()
            query = """
                UPDATE alumno_clase 
                SET id_equipamiento = %s
                WHERE id_clase = %s AND ci_alumno = %s
            """
            cursor.execute(query, (nuevo_id_equipamiento, id_clase, ci_alumno))
            self.conexion.commit()
            print(f"Inscripción del alumno {ci_alumno} en la clase {id_clase} modificada.")
        except mysql.connector.Error as e:
            print(f"Error al modificar inscripción: {e}")
        finally:
            cursor.close()

    def eliminar_inscripcion(self, id_clase, ci_alumno):
        """
        Eliminar la inscripción de un alumno en una clase.
        """
        try:
            cursor = self.conexion.cursor()
            query = """
                DELETE FROM alumno_clase
                WHERE id_clase = %s AND ci_alumno = %s
            """
            cursor.execute(query, (id_clase, ci_alumno))
            self.conexion.commit()
            print(f"Alumno {ci_alumno} eliminado de la clase {id_clase}.")
        except mysql.connector.Error as e:
            print(f"Error al eliminar inscripción: {e}")
        finally:
            cursor.close()

    def listar_alumnos_por_clase(self, id_clase):
        """
        Listar todos los alumnos inscritos en una clase.
        """
        try:
            cursor = self.conexion.cursor()
            query = """
                SELECT ci_alumno, id_equipamiento 
                FROM alumno_clase 
                WHERE id_clase = %s
            """
            cursor.execute(query, (id_clase,))
            alumnos = cursor.fetchall()

            if alumnos:
                print(f"Alumnos inscritos en la clase {id_clase}:")
                for alumno in alumnos:
                    ci, equipamiento = alumno
                    print(f" - CI: {ci}, Equipamiento: {equipamiento if equipamiento else 'Ninguno'}")
            else:
                print(f"No hay alumnos inscritos en la clase {id_clase}.")
        except mysql.connector.Error as e:
            print(f"Error al listar alumnos: {e}")
        finally:
            cursor.close()

    def listar_clases_por_alumno(self, ci_alumno):
        """
        Listar todas las clases en las que está inscrito un alumno.
        """
        try:
            cursor = self.conexion.cursor()
            query = """
                SELECT id_clase, id_equipamiento 
                FROM alumno_clase 
                WHERE ci_alumno = %s
            """
            cursor.execute(query, (ci_alumno,))
            clases = cursor.fetchall()

            if clases:
                print(f"Clases inscritas por el alumno {ci_alumno}:")
                for clase in clases:
                    id_clase, equipamiento = clase
                    print(f" - Clase ID: {id_clase}, Equipamiento: {equipamiento if equipamiento else 'Ninguno'}")
            else:
                print(f"El alumno {ci_alumno} no está inscrito en ninguna clase.")
        except mysql.connector.Error as e:
            print(f"Error al listar clases: {e}")
        finally:
            cursor.close()