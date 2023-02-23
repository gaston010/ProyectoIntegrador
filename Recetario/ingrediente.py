
class Ingredientes:
    _ingredientes_id: int = 0

    def __init__(self, nombre, cantidad, unidad_de_medida):
        self._nombre = nombre
        self._cantidad = cantidad
        self._unidad_de_medida = unidad_de_medida
        self._id_ingrediente = self.id_ing()

    @classmethod
    def id_ing(cls):
        cls._ingredientes_id += 1
        return cls._ingredientes_id

# ? DUDA IRA? �
    def __len__(self):
        return len(self._cantidad)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

    @property
    def unidad_de_medida(self):
        return self._unidad_de_medida

    @unidad_de_medida.setter
    def unidad_de_medida(self, unidad_de_medida):
        self._unidad_de_medida = unidad_de_medida

    def __str__(self):
        return f" Ingredientes {self._id_ingrediente} :\n Nombre: {self._nombre} Son {self._cantidad}:{self._unidad_de_medida} "


def agregar_ingrediente():
    ingredientes = []
    ing = ""
    if len(ingredientes) < 0 or ing =="fin".lower():
        print("No hay ingredientes, No se puede iniciar una receta sin ingredientes")
    else:
        while ing != "fin":
            ing = input("Ingresa el ingrediente: ")
            if ing != "fin":
                cant = input("Ingresa la cantidad: ")
                um = input("Ingresa la unidad de medida: ")
                ingredientes.append(Ingredientes({ing},{cant},{um}))

    for ingre in ingredientes:
        print(ingre)
