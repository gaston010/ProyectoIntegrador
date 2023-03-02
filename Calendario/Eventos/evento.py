
class Evento:
    """
    Clase que representa un evento en un calendario con fechas y nombres
    """
    id: int
    id= 0

    def __init__(self, nombre, fecha, hora):
        """_summary_

        Args:
            nombre (_type_): _description_
            fecha (_type_): _description_
        """
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.id= self.ente()

    
    @classmethod
    def ente(cls):
        """
        Genera un id para cada evento, solo genera un id si el evento es nuevo fecha y hora

        Returns:
            int: devuelve el valor en entero del id + 1
        """        
        cls.id += 1
        return cls.id

    

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self, hora):
        self.__hora = hora


    def agregar(self, nombre_evento, fecha, hora):
        import csv
        with open('eventos.csv', 'a+') as file:
            writer = csv.writer(file)
            writer.writerow([self.id, nombre_evento, fecha, hora])


    def eliminar(self, nombre_evento,):
        """
        Elimina un evento del calendario con el nombre del evento eso eliminara el mismo con la fecha incluida

        Args:
            nombre_evento (_type_): _description_
        """
        if self.nombre == nombre_evento:
            print(f"Evento {self.nombre} eliminado")
            self.nombre = None
            self.fecha = None

    def buscar_evento(self, nombre_evento):
        """_summary_

        Args:
            nombre_evento (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self.nombre == nombre_evento:
            return self.nombre

    def modificar_evento(self, nombre_evento, nuevo_nombre, nueva_fecha):
        """
        Modifica el nombre y la fecha de un evento el mismo tra la fecha para ser modificada

        Args:
            nombre_evento (_type_): Nombre del evento a modificar
            nuevo_nombre (_type_): Nuevo nombre del evento
            nueva_fecha (_type_): Nueva fecha del evento
        """
        if self.nombre == nombre_evento:
            self.nombre = nuevo_nombre
            self.fecha = nueva_fecha
            print(
                f"Evento {self.nombre} modificado, Su nueva fecha es {self.fecha}")

    def comprobar_fecha(self, fecha):
        """
        Comprueba si la fecha del evento es igual a una fecha anteriormente ingresada

        Args:
            fecha (_type_): _description_

        Returns:
            _type_: _description_
        """
        for fechas in self.fecha:
            if fechas == fecha:
                print("La fecha ya existe, por favor elija otra fecha")

    def __str__(self):
        return f"EventoID:{self.id}{self.nombre} - {self.fecha} - {self.hora}"



    """
    cargar_cvs:
    funciona cargando por medio de los parametros que se establecen,
    el nombre del evento, la fecha y la hora, luego se crea un archivo csv siempre y cuando el archivo exita de otra forma
    el mismo se crea y se le agregan los datos que se le pasan por parametro

    # ? ver como agregar una cabezar solo una vez
    # ! CORREGIR NO AGREGA UNA CABEZAR UNA UNICA VEZ!!!!!!!!!!!!!!!
    """

def cargar_csv(nombre, fecha, hora):
    evento = Evento(nombre, fecha, hora)
    import csv
    with open('eventos.csv', 'a+') as file:
        writer = csv.writer(file)
        writer.writerow([evento.id, evento.nombre, evento.fecha, evento.hora])

cargar_csv("Cumpleaños", "12/12/2020", "12:00")
