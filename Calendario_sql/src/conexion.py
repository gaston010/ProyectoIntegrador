import mysql.connector as mysql


class Conexion:

    def __init__(self):
        try:
            self.conexion = mysql.connect(
                host="localhost",
                user="root",
                password="root",
                database="eventosdb"
            )
            self.cursor = self.conexion.cursor()
            # muestra el nombre dela db
            print("Conectado a la base de datos", self.conexion.database)
        except mysql.Error as e:
            print("No se puede conectar", e)

    @staticmethod
    def create_database(self):
        sql = "CREATE DATABASE IF NOT EXISTS eventosdb"
        try:
            self.cursor.execute(sql)
            print("Base de datos creada")
        except mysql.Error as e:
            print("Error al crear la base de datos:", e)

    def createtable(self):
        sql = "CREATE TABLE IF NOT EXISTS eventos (nombre VARCHAR(50) NOT NULL, fecha DATE NOT NULL, hora TIME NOT NULL, descripcion VARCHAR(50), duracion VARCHAR(50) NOT NULL, importancia BOOLEAN NOT NULL, PRIMARY KEY (nombre))"
        try:
            self.cursor.execute(sql)
            print("Tabla creada")
        except mysql.Error as e:
            print("Error al crear la tabla:", e)

    def buscar(self, nombre):
        sql = f"SELECT * FROM eventos WHERE nombre LIKE '%{nombre}%'"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            resultado = list(resultado)
            return resultado
        except Exception as e:
            print("Error al buscar", e)
            return []

    def insertar(self, *datos):
        sql = "INSERT INTO eventos(nombre, fecha, hora, descripcion, duracion, importancia) VALUES(%s, %s, %s, %s, %s, %s)"
        try:
            self.cursor.execute(sql, datos)
            self.conexion.commit()
            print("Datos insertados")
        except Exception as e:
            print("Error al insertar", e)

    def eliminar(self, eliminar):
        sql = "DELETE FROM eventos WHERE nombre = %s"
        try:
            self.cursor.execute(sql, (eliminar,))
            self.conexion.commit()
            print("Datos eliminados")
        except Exception as e:
            print("Error al eliminar", e)

    def actualizar(self, *datos):
        sql = "UPDATE eventos SET nombre = %s, descripcion = %s, duracion = %s WHERE nombre = %s"
        try:
            self.cursor.execute(sql, (datos))
            self.conexion.commit()
            print("Datos actualizados")
        except Exception as e:
            print("Error al actualizar", e)

    def buscartodo(self):
        sql = "SELECT * FROM eventos"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            resultado = list(resultado)
            return resultado
        except Exception as e:
            print("Error al buscar", e)
            return []

    def buscarhora(self, hora):
        sql = f"SELECT * FROM eventos WHERE hora LIKE '%{hora}%'"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            resultado = list(resultado)
            return resultado
        except Exception as e:
            print("Error al buscar", e)
            return []

    def buscarfecha(self, fecha):
        sql = f"SELECT * FROM eventos WHERE fecha LIKE '%{fecha}%'"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            resultado = list(resultado)
            return resultado
        except Exception as e:
            print("Error al buscar", e)
            return []
