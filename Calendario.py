
from evento import Evento



class Calendario:

    def __init__(self, dias, nombre, fecha, descripcion, duracion,importancia):
        Evento.__init__(nombre, fecha, descripcion, duracion)
        self.__dias = dias
        self.__importancia = importancia
        
