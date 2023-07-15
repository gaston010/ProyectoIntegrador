
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
        except mysql.connector.Error as error:
            print("No se puede conectar", error)

    # falta corregir no se como hacer que se cree la base de datos antes de validar la conexion # noqa
    def createdb(self):
        if self.conexion:
            print("Conexión exitosa")
            sql = "CREATE DATABASE IF NOT EXISTS eventosdb"
            try:
                self.cursor.execute(sql)
                if self.cursor:
                    print("Base de datos creada")
                    self.etiqueta_tabla()
                    self.evento_tabla()
                    self.evento_etiqueta_tabla()
            except mysql.Error as e:
                print("Error al crear la base de datos:", e)

    # creaciones de la tablas , esto esta mal implementado pero realiza lo pensado # noqa
    def etiqueta_tabla(self):
        sql = "CREATE TABLE IF NOT EXISTS Etiquetas(idEtiqueta INT PRIMARY KEY AUTO_INCREMENT,etiqueta VARCHAR(255) NOT NULL);"
        try:
            self.cursor.execute(sql)
            if self.cursor:
                print("Tabla Etiquetas creada")
        except mysql.Error as e:
            print("Error al crear la tabla:", e)

    def evento_tabla(self):
        sql = "CREATE TABLE IF NOT EXISTS Eventos (idEvento INT PRIMARY KEY AUTO_INCREMENT,titulo VARCHAR(255) NOT NULL,fecha DATE NOT NULL,hora TIME NOT NULL,descripcion VARCHAR(255) NOT NULL, duracion VARCHAR(255) NULL,importancia TINYINT NULL);"
        try:
            self.cursor.execute(sql)
            if self.cursor:
                print("Tabla Eventos creada")
        except mysql.Error as e:
            print("Error al crear la tabla:", e)

    def evento_etiqueta_tabla(self):
        sql = "CREATE TABLE IF NOT EXISTS Etiqueta_Evento (idEtiqueta INT,idEvento INT,PRIMARY KEY (idEtiqueta, idEvento),FOREIGN KEY (idEtiqueta) REFERENCES Etiquetas(idEtiqueta),FOREIGN KEY (idEvento) REFERENCES Eventos(idEvento));"
        try:
            self.cursor.execute(sql)
            if self.cursor:
                print("Tabla Etiqueta_Evento creada")
        except mysql.Error as e:
            print("Error al crear la tabla:", e)

    def insertar(self, *datos):
        """
        Inserta un nuevo evento en la base de datos.

        Args:
        - datos (tuple): Tupla con los datos del evento a insertar.

        Returns:
        - None
        """
        sql = "INSERT INTO eventos(titulo, fecha, hora, descripcion, duracion, importancia) VALUES(%s, %s, %s, %s, %s, %s)"
        try:
            self.cursor.execute(sql, datos)
            self.conexion.commit()
            print("Datos insertados")
        except Exception as e:
            print("Error al insertar", e)

    def eliminar(self, eliminar):
        """
        Elimina un evento de la base de datos.

        Args:
        - eliminar (str): Titulo del evento a eliminar.

        Returns:
        - None
        """
        sql = "DELETE FROM eventos WHERE titulo = %s"
        try:
            self.cursor.execute(sql, (eliminar,))
            self.conexion.commit()
            print("Datos eliminados")
        except Exception as e:
            print("Error al eliminar", e)

    def actualizar(self, titulo, descripcion, duracion, id):
        sql = "UPDATE eventos SET titulo = %s , descripcion = %s , duracion = %s WHERE idEvento = %s"
        try:
            self.cursor.execute(sql, (titulo, descripcion, duracion, id))
            self.conexion.commit()
            print("Datos actualizados")
        except Exception as e:
            print("Error al actualizar", e)
        finally:
            self.cursor.close()
            self.conexion.close()

    def buscar(self, titulo):
        """
        Busca eventos en la base de datos que contengan el titulo especificado.

        Args:
        - titulo (str): Titulo del evento a buscar.

        Returns:
        - resultado (list): Lista con los eventos encontrados.
        """
        sql = f"SELECT * FROM eventos WHERE titulo LIKE '%{titulo}%'"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            resultado = list(resultado)
            return resultado
        except Exception as e:
            print("Error al buscar", e)
            return []

    def buscartodo(self):
        """
        Busca y devuelve todos los eventos registrados en la base de datos.

        Returns:
        - resultado (list): Lista de tuplas con los datos de los eventos encontrados.
        """
        sql = "SELECT * FROM eventos"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            resultado = list(resultado)
            return resultado
        except Exception as e:
            print("Error al buscar", e)
            return []

    # NO IMPLEMENTADO 2022-12-05

    def buscarhora(self, hora):
        """
        Busca y devuelve los eventos registrados en la base de datos que coinciden con la hora especificada.

        Args:
        - hora (str): Hora a buscar en formato HH:MM.

        Returns:
        - resultado (list): Lista de tuplas con los datos de los eventos encontrados.
        """
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
        """
        Busca y devuelve los eventos registrados en la base de datos que coinciden con la fecha especificada.

        Args:
        - fecha (str): Fecha a buscar en formato YYYY-MM-DD.

        Returns:
        - resultado (list): Lista de tuplas con los datos de los eventos encontrados.
        """
        sql = f"SELECT * FROM eventos WHERE fecha LIKE '%{fecha}%'"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            resultado = list(resultado)
            return resultado
        except Exception as e:
            print("Error al buscar", e)
            return []

    def buscarid(self, id):
        """
        Busca y devuelve los datos del evento registrado en la base de datos que coincide con el id especificado.

        Args:
        - id (int): Id del evento a buscar.

        Returns:
        - resultado (list): Lista de tuplas con los datos del evento encontrado.
        """
        sql = f"SELECT * FROM eventos WHERE idEvento = {id}"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            resultado = list(resultado)
            return resultado
        except Exception as e:
            print("Error al buscar", e)
            return []
