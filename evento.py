import tkinter as tk
from tkinter import ttk, messagebox

class Evento():

    id =0

    def __init__(self,root, nombre, fecha, hora, duracion=1):
        self.__nombre = nombre
        self.__fecha = fecha
        self.__hora = hora
        self.__duracion = duracion
        self.root = root
        self.__id = self.identificador()


    @classmethod
    def identificador(cls):
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

    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion

    # @staticmethod
    # def agregar_evento(nombre, fecha, hora, duracion):
    #     import csv
    #     with open('eventos.csv', 'a+') as archivo:
    #         archivo  = csv.writer(archivo)
    #         archivo.writerow([nombre, fecha, hora, duracion])

    def agregar_evento(self):
        import csv
        

    def __str__(self):
        return f'ID: {self.id} Nombre: {self.nombre} Fecha: {self.fecha} Hora: {self.hora} Duracion: {self.duracion} Hora'
        



""" esto es una pruba"""