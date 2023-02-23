"""
Recetario de cocina
Para este proyecto se deberá diseñar una aplicación de escritorio en la que puedan crear,
editar y eliminar recetas.
Una receta debe estar compuesta de los siguientes datos:
● Nombre. ✔️
● Una lista de los ingredientes. ✔️
● Preparación, lista ordenada de pasos a seguir. ✔️
● Imagen/es del plato preparado. Una receta puede o no tener una imagen. ✔️
● Tiempo de preparación (en minutos). ✔️
● Tiempo de cocción (en minutos). ✔️
● Fecha de creación. La fecha y hora en que se creó la receta en la aplicación. ✔️
● Etiquetas: palabras clave. ⭐
● Es favorita (o no). ⭐
Un ingrediente debe contar con la siguiente información:
● Nombre. ✔️
● Unidad de medida. ✔️
● Cantidad. ✔️
Las funcionalidades que debe tener la aplicación son las siguientes:
● Crear una receta. ✔️
● Modificar una receta. ✔️
● Eliminar una receta. ✔️
● Mostrar “receta del día” aleatoria en la ventana principal. ⭐
● Buscar y/o filtrar recetas:
○ Nombre. ⭐
○ Por etiquetas. ⭐
○ Tiempo de preparación. ⭐
○ Ingredientes. ⭐
Deberá contar con las siguientes vistas:
● Recetario. Ventana principal por defecto.
○ Se muestra un listado de todas las recetas. ✔️
○ Se mostrará como primera receta de lista a la “receta del día”, la cual debe
tener un formato distinto a las demás recetas. ⭐
● Muestra una receta ya existente. ✔️
● Carga/modificación de una receta. ✔️
● Búsqueda y filtro. La ventana deberá tener un campo de búsqueda, por nombre y/o
etiqueta. Una vez filtrados las recetas, se las mostrará en una lista.
    
"""


class Receta:
    def __init__(self, nombre, preparacion, tiempo, fecha, etiqueta, favorito, imagen):
        self._nombre = nombre
        self._preparacion = preparacion
        self._tiempo = tiempo
        self._fecha = fecha
        self._etiqueta = etiqueta
        self._favorito = favorito
        self._imagen = imagen

    def __str__(self):
        return f"Nombre: {self._nombre}\nPreparacion: {self._preparacion}\nTiempo: {self._tiempo}\nFecha: {self._fecha}\nEtiqueta: {self._etiqueta}\nFavorito: {self._favorito}\nImagen: {self._imagen}"

    def agregar_receta(self):
        pass

    def modificar_receta(self):
        pass

    def eliminar_receta(self):
        pass

    def mostrar_receta(self):
        pass

    def buscar_receta(self):
        pass

    def filtrar_receta(self):
        pass

    def receta_del_dia(self):
        pass

    def agregar_ingrediente(self):
        pass

    def modificar_ingrediente(self):
        pass

    def eliminar_ingrediente(self):
        pass

    def mostrar_ingrediente(self):
        pass

    def comprobar_preparacion(self):
        if self._preparacion == "":
            return "No se puede iniciar una receta sin preparacion"
        else:
            return "Receta iniciada"

    def comprobar_tiempo(self):
        if self._tiempo == "":
            return "No se puede iniciar una receta sin tiempo"
        else:
            return "Receta iniciada"

    def comprobar_fecha(self):
        if self._fecha == "":
            return "No se puede iniciar una receta sin fecha"
        else:
            return "Receta iniciada"

    def comprobar_nombre(self):
        if self._nombre == "":
            return "No se puede iniciar una receta sin nombre"
        else:
            return "Receta iniciada"

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

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

    @property
    def favorito(self):
        return self._favorito

    @favorito.setter
    def favorito(self, favorito):
        self._favorito = favorito

    @property
    def imagen(self):
        return self._imagen

    @imagen.setter
    def imagen(self, imagen):
        self._imagen = imagen
