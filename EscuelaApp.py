import mysql.connector
from login import Login
from instructorManager import InstructorManager
from turnoManager import TurnoManager
from reporte import Reporte
from alumnoManager import AlumnoManager
from equipamientoManager import EquipamientoManager
from actividadesManager import ActividadesManager
from claseManager import ClaseManager
from alumnoClaseManager import AlumnoClaseManager


# Clase principal para la aplicación
class EscuelaApp:
    def __init__(self, db_connection):
        self.login = Login(db_connection)
        self.instructor_manager = InstructorManager(db_connection)
        self.alumno_manager = AlumnoManager(db_connection)
        self.turno_manager = TurnoManager(db_connection)
        self.actividad_manager = ActividadesManager(db_connection)
        self.equipamiento_manager = EquipamientoManager(db_connection)
        self.clase_manager = ClaseManager(db_connection)
        self.alumnoclase_manager = AlumnoClaseManager(db_connection)
        self.reporte = Reporte(db_connection)

    def iniciar(self):
        correo = input("Correo: ")
        contraseña = input("Contraseña: ")
        if self.login.authenticate(correo, contraseña):
            while True:
                print("\n--- MENÚ PRINCIPAL ---")
                print("1. ABM Instructores")
                print("2. ABM Turnos")
                print("3. ABM Alumnos")
                print("4. Ver reportes")
                print("5. ABM Actividades")
                print("6. ABM Equipamientos")
                print("7. ABM Clases")
                print("8. Menu Inscripción de Alumnos")
                print("9. Salir")
                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    self.gestion_instructores()
                elif opcion == "2":
                    self.gestion_turnos()
                elif opcion == "3":
                    self.gestion_alumnos()
                elif opcion == "4":
                    self.ver_reportes()
                elif opcion == "5":
                    self.gestion_actividades()
                elif opcion == "6":
                    self.gestion_equipamiento()
                elif opcion == "7":
                    self.gestion_clases()
                elif opcion == "8":
                    self.gestion_inscripcion_alumnos()
                elif opcion == "9":
                    self.login.logout(correo)
                    break
                else:
                    print("Opción inválida.")

    # Gestión de Instructores
    def gestion_instructores(self):
        while True:
            print("\n--- ABM Instructores ---")
            print("1. Agregar Instructor")
            print("2. Modificar Instructor")
            print("3. Eliminar Instructor")
            print("4. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                ci = input("Ingrese la CI del instructor: ")
                nombre = input("Ingrese el nombre: ")
                apellido = input("Ingrese el apellido: ")
                self.instructor_manager.agregar_instructor(ci, nombre, apellido)
            elif opcion == "2":
                ci = input("Ingrese la CI del instructor a modificar: ")
                nombre = input("Nuevo nombre (deje en blanco si no quiere cambiarlo): ")
                apellido = input("Nuevo apellido (deje en blanco si no quiere cambiarlo): ")
                self.instructor_manager.modificar_instructor(ci, nombre if nombre else None, apellido if apellido else None)
            elif opcion == "3":
                ci = input("Ingrese la CI del instructor a eliminar: ")
                self.instructor_manager.eliminar_instructor(ci)
            elif opcion == "4":
                break
            else:
                print("Opción inválida.")

    # Gestión de Alumnos
    def gestion_alumnos(self):
        while True:
            print("\n--- ABM Alumnos ---")
            print("1. Agregar Alumno")
            print("2. Modificar Alumno")
            print("3. Eliminar Alumno")
            print("4. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                ci = input("Ingrese la CI del alumno: ")
                nombre = input("Ingrese el nombre: ")
                apellido = input("Ingrese el apellido: ")
                fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
                telefono = input("Ingrese el teléfono: ")
                correo = input("Ingrese el correo electrónico: ")
                self.alumno_manager.alta_alumno(ci, nombre, apellido, fecha_nacimiento, telefono, correo)
            elif opcion == "2":
                ci = input("Ingrese la CI del alumno a modificar: ")
                nombre = input("Nuevo nombre (deje en blanco si no quiere cambiarlo): ")
                apellido = input("Nuevo apellido (deje en blanco si no quiere cambiarlo): ")
                fecha_nacimiento = input("Nueva fecha de nacimiento (deje en blanco): ")
                telefono = input("Nuevo teléfono (deje en blanco): ")
                correo = input("Nuevo correo electrónico (deje en blanco): ")
                self.alumno_manager.modificar_alumno(
                    ci, 
                    nombre if nombre else None, 
                    apellido if apellido else None, 
                    fecha_nacimiento if fecha_nacimiento else None,
                    telefono if telefono else None, 
                    correo if correo else None
                )
            elif opcion == "3":
                ci = input("Ingrese la CI del alumno a eliminar: ")
                self.alumno_manager.baja_alumno(ci)
            elif opcion == "4":
                break
            else:
                print("Opción inválida.")
        
    # Gestión de Turnos
    def gestion_turnos(self):
        while True:
            print("\n--- ABM Turnos ---")
            print("1. Agregar Turno")
            print("2. Modificar Turno")
            print("3. Eliminar Turno")
            print("4. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                hora_inicio = input("Ingrese la hora de inicio (HH:MM): ")
                hora_fin = input("Ingrese la hora de fin (HH:MM): ")
                self.turno_manager.agregar_turno(hora_inicio, hora_fin)
            elif opcion == "2":
                id_turno = input("Ingrese el ID del turno a modificar: ")
                hora_inicio = input("Nueva hora de inicio (deje en blanco): ")
                hora_fin = input("Nueva hora de fin (deje en blanco): ")
                self.turno_manager.modificar_turno(
                    id_turno, 
                    hora_inicio if hora_inicio else None, 
                    hora_fin if hora_fin else None
                )
            elif opcion == "3":
                id_turno = input("Ingrese el ID del turno a eliminar: ")
                self.turno_manager.eliminar_turno(id_turno)
            elif opcion == "4":
                break
            else:
                print("Opción inválida.")

    # Ver reportes
    def ver_reportes(self):
        while True:
            print("\n--- Reportes ---")
            print("1. Actividades con más ingresos")
            print("2. Actividades con más alumnos")
            print("3. Turnos con más clases dictadas")
            print("4. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.reporte.reporte_actividades_mas_ingresos()
            elif opcion == "2":
                self.reporte.reporte_actividades_con_mas_alumnos()
            elif opcion == "3":
                self.reporte.reporte_turnos_con_mas_clases_dictadas()
            elif opcion == "4":
                break
            else:
                print("Opción inválida.")
                
    def gestion_clases(self):
        while True:
            print("\n1. Agregar Clase")
            print("2. Modificar Clase")
            print("3. Eliminar Clase")
            print("4. Listar Clases")
            print("5. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                ci_instructor = input("CI del Instructor: ")
                id_actividad = int(input("ID de la Actividad: "))
                id_turno = int(input("ID del Turno: "))
                self.clase_manager.agregar_clase(ci_instructor, id_actividad, id_turno)
            elif opcion == "2":
                id_clase = int(input("ID de la Clase a modificar: "))
                ci_instructor = input("Nuevo CI del Instructor (dejar en blanco para no modificar): ") or None
                id_actividad = input("Nuevo ID de la Actividad (dejar en blanco para no modificar): ") or None
                id_turno = input("Nuevo ID del Turno (dejar en blanco para no modificar): ") or None
                dictada = input("Clase dictada? (si/no, dejar en blanco para no modificar): ").lower()
                dictada = True if dictada == "si" else False if dictada == "no" else None
                self.clase_manager.modificar_clase(id_clase, ci_instructor, id_actividad, id_turno, dictada)
            elif opcion == "3":
                id_clase = int(input("ID de la Clase a eliminar: "))
                self.clase_manager.eliminar_clase(id_clase)
            elif opcion == "4":
                self.clase_manager.listar_clases()
            elif opcion == "5":
                break
            else:
                print("Opción inválida.")
    
    def gestion_actividades(self):
        """
        Menú para gestionar las actividades.
        """
        while True:
            print("\n--- Gestión de Actividades ---")
            print("1. Agregar actividad")
            print("2. Modificar actividad")
            print("3. Eliminar actividad")
            print("4. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.agregar_actividad()
            elif opcion == "2":
                self.modificar_actividad()
            elif opcion == "3":
                self.eliminar_actividad()
            elif opcion == "4":
                break
            else:
                print("Opción no válida. Intente nuevamente.")
    
    def agregar_actividad(self):
        descripcion = input("Ingrese la descripción de la actividad: ")
        costo = float(input("Ingrese el costo de la actividad: "))
        self.actividad_manager.agregar_actividad(descripcion, costo)
    
    def modificar_actividad(self):
        actividad_id = int(input("Ingrese el ID de la actividad a modificar: "))
        nueva_descripcion = input("Ingrese la nueva descripción (o deje en blanco para no cambiar): ")
        nuevo_costo = input("Ingrese el nuevo costo (o deje en blanco para no cambiar): ")
        nuevo_costo = float(nuevo_costo) if nuevo_costo else None
        self.actividad_manager.modificar_actividad(actividad_id, nueva_descripcion, nuevo_costo)
    
    def eliminar_actividad(self):
        actividad_id = int(input("Ingrese el ID de la actividad a eliminar: "))
        self.actividad_manager.eliminar_actividad(actividad_id)
    
    def gestion_inscripcion_alumnos(self):
        """
        Menú para gestionar las inscripciones de alumnos en clases.
        """
        while True:
            print("\n--- GESTIÓN DE INSCRIPCIONES DE ALUMNOS ---")
            print("1. Inscribir Alumno en Clase")
            print("2. Modificar Inscripción de Alumno")
            print("3. Eliminar Inscripción")
            print("4. Listar Alumnos por Clase")
            print("5. Listar Clases por Alumno")
            print("6. Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.inscribir_alumno()
            elif opcion == "2":
                self.modificar_inscripcion()
            elif opcion == "3":
                self.eliminar_inscripcion()
            elif opcion == "4":
                self.listar_alumnos_por_clase()
            elif opcion == "5":
                self.listar_clases_por_alumno()
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")

    def inscribir_alumno(self):
        try:
            id_clase = int(input("Ingrese el ID de la clase: "))
            ci_alumno = input("Ingrese la cédula del alumno: ")
            id_equipamiento = input("Ingrese el ID del equipamiento (opcional, presione Enter si no aplica): ")
            id_equipamiento = int(id_equipamiento) if id_equipamiento else None

            self.alumno_clase_manager.inscribir_alumno(id_clase, ci_alumno, id_equipamiento)
        except ValueError:
            print("Entrada no válida. Asegúrese de ingresar datos correctos.")

    def modificar_inscripcion(self):
        try:
            id_clase = int(input("Ingrese el ID de la clase: "))
            ci_alumno = input("Ingrese la cédula del alumno: ")
            nuevo_id_equipamiento = input("Ingrese el nuevo ID del equipamiento (opcional, presione Enter si no aplica): ")
            nuevo_id_equipamiento = int(nuevo_id_equipamiento) if nuevo_id_equipamiento else None

            self.alumno_clase_manager.modificar_inscripcion(id_clase, ci_alumno, nuevo_id_equipamiento)
        except ValueError:
            print("Entrada no válida. Asegúrese de ingresar datos correctos.")

    def eliminar_inscripcion(self):
        try:
            id_clase = int(input("Ingrese el ID de la clase: "))
            ci_alumno = input("Ingrese la cédula del alumno: ")
            self.alumno_clase_manager.eliminar_inscripcion(id_clase, ci_alumno)
        except ValueError:
            print("Entrada no válida. Asegúrese de ingresar datos correctos.")

    def listar_alumnos_por_clase(self):
        try:
            id_clase = int(input("Ingrese el ID de la clase: "))
            self.alumno_clase_manager.listar_alumnos_por_clase(id_clase)
        except ValueError:
            print("Entrada no válida. Asegúrese de ingresar datos correctos.")

    def listar_clases_por_alumno(self):
        ci_alumno = input("Ingrese la cédula del alumno: ")
        self.alumno_clase_manager.listar_clases_por_alumno(ci_alumno)

    def gestion_equipamiento(self):
        """
        Menú para gestionar el equipamiento.
        """
        while True:
            print("\n--- Gestión de Equipamiento ---")
            print("1. Agregar equipamiento")
            print("2. Modificar equipamiento")
            print("3. Eliminar equipamiento")
            print("4. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.agregar_equipamiento()
            elif opcion == "2":
                self.modificar_equipamiento()
            elif opcion == "3":
                self.eliminar_equipamiento()
            elif opcion == "4":
                break
            else:
                print("Opción no válida. Intente nuevamente.")
    
    def agregar_equipamiento(self):
        id_actividad = int(input("Ingrese el ID de la actividad asociada: "))
        descripcion = input("Ingrese la descripción del equipamiento: ")
        costo = float(input("Ingrese el costo del equipamiento: "))
        self.equipamiento_manager.agregar_equipamiento(id_actividad, descripcion, costo)
    
    def modificar_equipamiento(self):
        equipamiento_id = int(input("Ingrese el ID del equipamiento a modificar: "))
        nueva_descripcion = input("Ingrese la nueva descripción (o deje en blanco para no cambiar): ")
        nuevo_costo = input("Ingrese el nuevo costo (o deje en blanco para no cambiar): ")
        nuevo_costo = float(nuevo_costo) if nuevo_costo else None
        self.equipamiento_manager.modificar_equipamiento(equipamiento_id, nueva_descripcion, nuevo_costo)
    
    def eliminar_equipamiento(self):
        equipamiento_id = int(input("Ingrese el ID del equipamiento a eliminar: "))
        self.equipamiento_manager.eliminar_equipamiento(equipamiento_id)

                
                
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