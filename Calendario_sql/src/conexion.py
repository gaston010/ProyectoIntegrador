import sqlite3 as sql
import datetime as dt


class Conexion:

    def __init__(self, ):
        self.db = "calendario.sqlite3"
        self.fecha = dt.datetime.now().strftime("%Y-%m-%d")
        self.hora = dt.datetime.now().strftime("%H:%M")

    def tabla(self):
        self.conectar()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Eventos (id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT, fecha DATE, hora TIME, descripcion TEXT, importancia BOOLEAN)")
        self.desconectar()

    def conectar(self):
        self.conexion = sql.connect(self.db)
        self.cursor = self.conexion.cursor()

    def desconectar(self):
        self.conexion.close()
    
    def insertar(self,*datos):
        self.conectar()
        self.cursor.execute("INSERT INTO Eventos VALUES (?, ?, ?, ?, ?)",datos)
        self.conexion.commit()
        self.desconectar()

    def borrar(self, id):
        self.conectar()
        self.cursor.execute("DELETE FROM Eventos WHERE id = ?", (id,))
        self.conexion.commit()
        self.desconectar()

    def actualizar(self, id, nombre, fecha, hora, descripcion, importancia):
        self.conectar()
        self.cursor.execute("UPDATE Eventos SET nombre = ?, fecha = ?, hora = ?, descripcion = ?, importancia = ? WHERE id = ?", (nombre, fecha, hora, descripcion, importancia, id))
        self.conexion.commit()
        self.desconectar()

Conexion().tabla()

Conexion().insertar("Prueba", "2020-12-12", "12:00", "Prueba de inserción", True)