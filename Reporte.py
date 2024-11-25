# Clase para los reportes
class Reporte:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def reporte_actividades_mas_ingresos(self):
        cursor = self.db_connection.cursor(dictionary=True)
        query = """
        SELECT a.descripcion, IFNULL(SUM(a.costo + e.costo), 0) AS total_ingreso
        FROM actividades a
        LEFT JOIN equipamiento e ON a.id = e.id_actividad
        LEFT JOIN clase c ON a.id = c.id_actividad
        LEFT JOIN alumno_clase ac ON c.id = ac.id_clase
        WHERE ac.ci_alumno IS NOT NULL
        GROUP BY a.id
        ORDER BY total_ingreso DESC
        """
        cursor.execute(query)
        resultados = cursor.fetchall()
        for row in resultados:
            print(f"Actividad: {row['descripcion']}, Ingreso total: {row['total_ingreso']}")
    
    def reporte_actividades_con_mas_alumnos(self):
        cursor = self.db_connection.cursor(dictionary=True)
        query = """
        SELECT a.descripcion, COUNT(ac.ci_alumno) AS total_alumnos
        FROM actividades a
        JOIN clase c ON a.id = c.id_actividad
        JOIN alumno_clase ac ON c.id = ac.id_clase
        GROUP BY a.id
        ORDER BY total_alumnos DESC
        """
        cursor.execute(query)
        resultados = cursor.fetchall()
        for row in resultados:
            print(f"Actividad: {row['descripcion']}, Total alumnos: {row['total_alumnos']}")

    def reporte_turnos_con_mas_clases_dictadas(self):
        cursor = self.db_connection.cursor(dictionary=True)
        query = """
        SELECT t.id, t.hora_inicio, t.hora_fin, COUNT(c.id) AS total_clases
        FROM turnos t
        JOIN clase c ON t.id = c.id_turno
        WHERE c.dictada = TRUE
        GROUP BY t.id
        ORDER BY total_clases DESC
        """
        cursor.execute(query)
        resultados = cursor.fetchall()
        for row in resultados:
            print(f"Turno: {row['id']}, Inicio: {row['hora_inicio']}, Fin: {row['hora_fin']}, Clases dictadas: {row['total_clases']}")
