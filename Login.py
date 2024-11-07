import mysql.connector

# Clase para conexión y autenticación de usuario
class Login:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def authenticate(self, correo, contraseña):
        cursor = self.db_connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM login WHERE correo = %s AND contraseña = %s", (correo, contraseña))
        user = cursor.fetchone()
        if user:
            cursor.execute("UPDATE login SET Actividad = TRUE WHERE correo = %s", (correo,))
            self.db_connection.commit()
            print("Login exitoso. Bienvenido!")
            return True
        else:
            print("Credenciales incorrectas.")
            return False

    def logout(self, correo):
        cursor = self.db_connection.cursor()
        cursor.execute("UPDATE login SET Actividad = FALSE WHERE correo = %s", (correo,))
        self.db_connection.commit()
        print("Sesión cerrada.")