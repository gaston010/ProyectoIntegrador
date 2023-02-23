from ingrediente import *


class Receta(Ingredientes):
    id_receta: int = 0

    def __init__(self, nombre, cantidad, unidad_de_medida, preparacion, tiempo, fecha, etiqueta=None, favorito=False, imagen=None):
        Ingredientes.__init__(self, nombre, cantidad, unidad_de_medida)
        self._preparacion = preparacion
        self._tiempo = tiempo
        self._fecha = fecha
        self._etiqueta = etiqueta
        self._favorito = favorito
        self.id_receta = self.id_rec()

    @classmethod
    def id_rec(cls):
        cls.id_receta += 1
        return cls.id_receta

    @property
    def preparacion(self):
        return self._preparacion

    @preparacion.setter
    def preparacion(self, preparacion):
        self._preparacion = preparacion

    @property
    def tiempo(self):
        return self._tiempo

    @tiempo.setter
    def tiempo(self, tiempo):
        self._tiempo = tiempo

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def etiqueta(self):
        return self._etiqueta

    @etiqueta.setter
    def etiqueta(self, etiqueta):
        self._etiqueta = etiqueta

    def __str__(self):
        return Ingredientes.__str__(self)

    def comprobar_preparacion(self):
        if self._preparacion == "":
            return "No se puede iniciar una receta sin preparacion"
        else:
            return "Receta iniciada"


def agregar_receta(receta_nombre):
    rec = ""
    ing = agregar_ingrediente()
    while rec != "fin".lower():
        print("Ingresa los datos de la receta")
        receta_nombre = input("Ingresa el nombre de la receta: ")
        print(f"R")
