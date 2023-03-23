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

    def borrar(self, nombre):
        self.conectar()
        self.cursor.execute("DELETE FROM Eventos WHERE nombre  = ?", (nombre,))
        self.conexion.commit()
        self.desconectar()

    def actualizar(self, remplzar, nombre):
        self.conectar()
        self.update = "UPDATE Eventos SET Nombre = ?, WHERE Nombre = ?",(remplzar, nombre)
        self.conexion.commit()
        self.desconectar()


Conexion().actualizar("Cena", "Comer")