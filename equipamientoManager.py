class EquipamientoManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def agregar_equipamiento(self, id_actividad, descripcion, costo):
        """
        Agrega un nuevo equipamiento a la base de datos.
        """
        try:
            cursor = self.db_connection.cursor()
            query = """
                INSERT INTO equipamiento (id_actividad, descripcion, costo)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (id_actividad, descripcion, costo))
            self.db_connection.commit()
            print("Equipamiento agregado exitosamente.")
        except Exception as e:
            print(f"Error al agregar equipamiento: {e}")
            self.db_connection.rollback()

    def modificar_equipamiento(self, equipamiento_id, nueva_descripcion=None, nuevo_costo=None):
        """
        Modifica un equipamiento existente.
        Puede actualizar la descripción, el costo, o ambos.
        """
        if not nueva_descripcion and nuevo_costo is None:
            print("No se proporcionó ninguna modificación.")
            return
        
        try:
            cursor = self.db_connection.cursor()
            query = "UPDATE equipamiento SET "
            params = []

            # Construcción dinámica del query en función de los parámetros
            if nueva_descripcion:
                query += "descripcion = %s, "
                params.append(nueva_descripcion)
            if nuevo_costo is not None:
                query += "costo = %s, "
                params.append(nuevo_costo)

            query = query.rstrip(", ")  # Eliminar la última coma
            query += " WHERE id = %s"
            params.append(equipamiento_id)

            cursor.execute(query, tuple(params))
            self.db_connection.commit()
            print("Equipamiento modificado exitosamente.")
        except Exception as e:
            print(f"Error al modificar equipamiento: {e}")
            self.db_connection.rollback()

    def obtener_equipamiento(self, equipamiento_id):
        """
        Obtiene un equipamiento específico por su ID.
        """
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM equipamiento WHERE id = %s"
            cursor.execute(query, (equipamiento_id,))
            equipamiento = cursor.fetchone()
            if equipamiento:
                print("Equipamiento encontrado:", equipamiento)
                return equipamiento
            else:
                print("Equipamiento no encontrado.")
                return None
        except Exception as e:
            print(f"Error al obtener equipamiento: {e}")
            return None

    def obtener_equipamiento_por_actividad(self, id_actividad):
        """
        Obtiene todos los equipamientos asociados a una actividad específica.
        """
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM equipamiento WHERE id_actividad = %s"
            cursor.execute(query, (id_actividad,))
            equipamientos = cursor.fetchall()
            if equipamientos:
                print(f"Equipamientos encontrados para la actividad {id_actividad}:")
                for equip in equipamientos:
                    print(equip)
                return equipamientos
            else:
                print("No se encontraron equipamientos para esta actividad.")
                return []
        except Exception as e:
            print(f"Error al obtener equipamientos: {e}")
            return []