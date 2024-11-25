class ActividadesManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def crear_actividad(self, descripcion, costo):
        """
        Crea una nueva actividad en la base de datos.
        """
        try:
            cursor = self.db_connection.cursor()
            query = """
                INSERT INTO actividades (descripcion, costo)
                VALUES (%s, %s)
            """
            cursor.execute(query, (descripcion, costo))
            self.db_connection.commit()
            print("Actividad creada exitosamente.")
        except Exception as e:
            print(f"Error al crear actividad: {e}")
            self.db_connection.rollback()

    def modificar_actividad(self, actividad_id, nueva_descripcion=None, nuevo_costo=None):
        """
        Modifica una actividad existente en la base de datos.
        Puede modificar la descripción, el costo, o ambos.
        """
        if not nueva_descripcion and not nuevo_costo:
            print("No se proporcionó ninguna modificación.")
            return
        
        try:
            cursor = self.db_connection.cursor()
            query = "UPDATE actividades SET "
            params = []
            
            # Generar el query dinámicamente según los parámetros proporcionados
            if nueva_descripcion:
                query += "descripcion = %s, "
                params.append(nueva_descripcion)
            if nuevo_costo:
                query += "costo = %s, "
                params.append(nuevo_costo)
            
            query = query.rstrip(", ")  # Eliminar la última coma
            query += " WHERE id = %s"
            params.append(actividad_id)
            
            cursor.execute(query, tuple(params))
            self.db_connection.commit()
            print("Actividad modificada exitosamente.")
        except Exception as e:
            print(f"Error al modificar actividad: {e}")
            self.db_connection.rollback()

    def obtener_actividad(self, actividad_id):
        """
        Obtiene los detalles de una actividad por su ID.
        """
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM actividades WHERE id = %s"
            cursor.execute(query, (actividad_id,))
            actividad = cursor.fetchone()
            if actividad:
                print("Actividad encontrada:", actividad)
                return actividad
            else:
                print("Actividad no encontrada.")
        except Exception as e:
            print(f"Error al obtener actividad: {e}")
            return None
        
    def eliminar_actividad(self, actividad_id):
        """
        Elimina una actividad existente de la base de datos por su ID.
        """
        try:
            cursor = self.db_connection.cursor()
            query = "DELETE FROM actividades WHERE id = %s"
            cursor.execute(query, (actividad_id,))
            if cursor.rowcount > 0:
                self.db_connection.commit()
                print("Actividad eliminada exitosamente.")
            else:
                print("No se encontró ninguna actividad con el ID proporcionado.")
        except Exception as e:
            print(f"Error al eliminar actividad: {e}")
            self.db_connection.rollback()