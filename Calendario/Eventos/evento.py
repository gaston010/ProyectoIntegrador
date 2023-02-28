
class Evento:
    """
    Clase que representa un evento en un calendario con fechas y nombres
    """
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
        self.id = self.asignar_id()

    @classmethod
    def asignar_id(cls):
        """
         carga los valores de evento dentro de la clase

        Returns:
            int: valores del evonto_id
        """
        cls.id += 1
        print(cls.id)
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
        return f"EventoID:{self.id} {self.nombre} - {self.fecha} - {self.hora}"


def nuevo_evento(nombre,fecha,hora):
    """
    Crea un nuevo evento

    Args:
        nombre (_type_): _description_
        fecha (_type_): _description_
    """
    import json
    evento = Evento(nombre, fecha, hora)
    if hora < 24:
        with open("eventos.json", "a+") as archivo:
            archivo.write(json.dumps(evento.__dict__))
            archivo.write(" ")
            
    else:
        print(f"Evento {evento.nombre} creado con exito")
        return evento
        
nuevo_evento("PARTELOS", "2021-10-10", 23)