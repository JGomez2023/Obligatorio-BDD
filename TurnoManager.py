# Clase para manejar turnos
class TurnoManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def agregar_turno(self, hora_inicio, hora_fin):
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO turnos (hora_inicio, hora_fin) VALUES (%s, %s)", (hora_inicio, hora_fin))
        self.db_connection.commit()
        print("Turno agregado con éxito.")

    def eliminar_turno(self, id):
        cursor = self.db_connection.cursor()
        cursor.execute("DELETE FROM turnos WHERE id = %s", (id,))
        self.db_connection.commit()
        print("Turno eliminado con éxito.")

    def modificar_turno(self, id, hora_inicio=None, hora_fin=None):
        cursor = self.db_connection.cursor()
        if hora_inicio:
            cursor.execute("UPDATE turnos SET hora_inicio = %s WHERE id = %s", (hora_inicio, id))
        if hora_fin:
            cursor.execute("UPDATE turnos SET hora_fin = %s WHERE id = %s", (hora_fin, id))
        self.db_connection.commit()
        print("Turno modificado con éxito.")