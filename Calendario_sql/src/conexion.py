import sqlite3 as sql
import datetime as dt
import mysql.connector as mysql

class Conexion:

    def __init__(self, ):
        try:
            self.conexion = mysql.connect( 
            host = "localhost",
            user = "root",
            password = "root",
            database = "eventosdb"
        )
            self.cursor = self.conexion.cursor()
            print(f"Conectado a la base de datos", self.conexion.database) # muestra el nombre dela db
        except sql.Error as e:
            print("No se puede conectar")

    
    def buscar(self, nombre):
        sql = f"SELECT * FROM eventos WHERE nombre LIKE '%{nombre}%'"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            resultado = list(resultado)
            return resultado
        except Exception  as e:
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
            self.cursor.execute(sql, eliminar)
            self.conexion.commit()
            print("Datos eliminados")
        except Exception as e:
            print("Error al eliminar", e)


    def actualizar(self, *datos):
        sql = "UPDATE eventos SET nombre = %s, descripcion = %s, duracion %s  WHERE nombre = %s"
        try:
            self.cursor.execute(sql, datos)
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

    def buscarhora(self,hora):
        sql = f"SELECT * FROM eventos WHERE hora LIKE '%{hora}%'"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            resultado = list(resultado)
            return resultado
        except Exception  as e:
            print("Error al buscar", e)
            return []

