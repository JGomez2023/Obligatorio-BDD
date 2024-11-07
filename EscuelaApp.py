import mysql.connector
from login import Login
from instructorManager import InstructorManager
from turnoManager import TurnoManager
from reporte import Reporte
from alumnoManager import AlumnoManager


# Clase principal para la aplicación
class EscuelaApp:
    def __init__(self, db_connection):
        self.login = Login(db_connection)
        self.instructor_manager = InstructorManager(db_connection)
        self.alumno_manager = AlumnoManager(db_connection)
        self.turno_manager = TurnoManager(db_connection)
        self.reporte = Reporte(db_connection)

    def iniciar(self):
        correo = input("Correo: ")
        contraseña = input("Contraseña: ")
        if self.login.authenticate(correo, contraseña):
            while True:
                print("\n1. ABM Instructores")
                print("2. ABM Turnos")
                print("3. ABM Alumnos")
                print("4. Ver reportes")
                print("5. Salir")
                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    self.gestion_instructores()
                elif opcion == "2":
                    self.gestion_turnos()
                elif opcion == "3":
                    self.ver_reportes()
                elif opcion == "4":
                    self.login.logout(correo)
                    break
                else:
                    print("Opción inválida.")

    def gestion_instructores(self):
        print("\n1. Agregar Instructor")
        print("2. Modificar Instructor")
        print("3. Eliminar Instructor")
        # Implementar lógica según la opción

    def gestion_alumnos(self):
        print("\n1. Agregar Alumno")
        print("2. Modificar Alumno")
        print("3. Eliminar Alumno")
        # Implementar lógica según la opción
        
    def gestion_turnos(self):
        print("\n1. Agregar Turno")
        print("2. Modificar Turno")
        print("3. Eliminar Turno")
        # Implementar lógica según la opción

    def ver_reportes(self):
        print("\n1. Actividades con más ingresos")
        print("2. Actividades con más alumnos")
        print("3. Turnos con más clases dictadas")
        # Implementar lógica para mostrar reportes

# Conexión a la base de datos y ejecución
if __name__ == "__main__":
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="escuela_deportes"
    )
    app = EscuelaApp(db_connection)
    app.iniciar()
    db_connection.close()