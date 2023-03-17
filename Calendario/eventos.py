import tkinter as tk
from tkinter import messagebox,ttk
import csv
import datetime as dt

class Evento:
    id_evento = 0

    def __init__(self, root):
        self.root = root
        root.title("Formulario de eventos")

        # Definir variables de control
        self.titulo_var = tk.StringVar()
        self.fecha_var = tk.StringVar()
        self.hora_var = tk.StringVar()
        self.descripcion_var = tk.StringVar()
        self.duracion = tk.StringVar()
        self.importancia_var = tk.BooleanVar()


        self.buscar = tk.StringVar()
        #self.id_evento = self.identificador() # no usado una forma mejor que no rompe las guindas



        # obtener la fecha y la hora actual
        fecha_actual = dt.date.today()
        self.fecha_var.set(fecha_actual.strftime("%d/%m/%Y"))

        hora_actual = dt.datetime.now().time()
        self.hora_var.set(hora_actual.strftime("%H:%M"))
        
        self.duracion.set("1 hora")


        # Crear etiquetas y campos de entrada
        tk.Label(root, text="Título:").grid(row=0, column=0)
        tk.Entry(root,textvariable=self.titulo_var).grid(row=0, column=1)
        
        tk.Label(root, text="Fecha (DD/MM/AAAA):",).grid(row=1, column=0)
        tk.Entry(root, textvariable=self.fecha_var).grid(row=1, column=1)

        tk.Label(root, text="Hora (HH:MM):").grid(row=2, column=0)
        tk.Entry(root, textvariable=self.hora_var).grid(row=2, column=1)

        tk.Label(root, text="Descripción:").grid(row=3, column=0)
        tk.Entry(root, textvariable=self.descripcion_var).grid(row=3, column=1)

        tk.Label(root, text="Importancia:").grid(row=5, column=0)
        tk.Checkbutton(root, variable=self.importancia_var).grid(row=5, column=1)

        tk.Label(root, text="Duracion:").grid(row=4, column=0)
        tk.Entry(root, textvariable=self.duracion).grid(row=4, column=1)

        tk.Label(root, text="Buscar Evento:").grid(row=0, column=2)
        tk.Entry(root, textvariable=self.buscar).grid(row=0, column=3)

        # Crear botones
        tk.Button(root, text="Crear Nuevo Evento", command=self.guardar).grid(row=6, column=0)
        tk.Button(root, text="Modificar", command=self.modificar).grid(row=7, column=0)
        tk.Button(root, text="Eliminar evento", command=self.eliminar_evento).grid(row=6, column=2)
        tk.Button(root, text="Buscar", command=self.buscar_evento).grid(row=1, column=3)


# FUNCIONAL NO TOCAR
    def eliminar_evento(self):
        # Obtener el título del evento a eliminar
        titulo = self.titulo_var.get()

        if titulo == "":
            messagebox.showwarning("Error", "El título es obligatorio use el boton buscar")
            return
        else:


            # Leer los eventos desde el archivo CSV
            eventos = []
            with open("eventos.csv", newline="") as archivo:
                contenido = csv.reader(archivo)
                for row in contenido:
                    if row[0] != titulo:  # si el título no coincide, agregar el evento a la lista
                        eventos.append(row)

            # Escribir los eventos actualizados al archivo CSV
            with open("eventos.csv", "w", newline="") as archivo:
                contenido = csv.writer(archivo)
                contenido.writerows(eventos)

            # Limpiar los campos de entrada
            fecha_actual = dt.date.today()
            hora_actual = dt.datetime.now().time()
            self.titulo_var.set("")
            self.fecha_var.set(fecha_actual.strftime("%d/%m/%Y"))
            self.hora_var.set(hora_actual.strftime("%H:%M"))
            self.descripcion_var.set("")
            self.duracion.set("1 Hora")
            self.importancia_var.set(False)
            

# esto ya anda no TOCAR
    def guardar(self):
        # genera la hora y le facha actual para poder ser usado dendtro de un ser guardaro y limpie los campos
        fecha_actual = dt.date.today()
        hora_actual = dt.datetime.now().time()
        
        # Comprueba si el titulo esta vacio
        if self.titulo_var.get() == "":
            messagebox.showwarning("Error", "El título es obligatorio")
            return
        elif self.comprobar_hora():
            messagebox.showwarning("Error", "Contiene evento en el mismo horario")
            return
        else:
            data = [
                self.titulo_var.get(),
                self.fecha_var.get(),
                self.hora_var.get(),
                self.descripcion_var.get(),
                self.duracion.get(),
                self.importancia_var.get()
            ]
            cabecera = ["Titulo", "Fecha", "Hora", "Descripcion", "Duracion", "Importancia"]
            with open("eventos.csv", "a", newline="") as archivo:
                contenido = csv.writer(archivo)
                if archivo.tell() == 0:
                    contenido.writerow(cabecera)
                contenido.writerow(data)
                messagebox.showinfo("Información", "Evento guardado correctamente")
                
                self.titulo_var.set("")
                self.fecha_var.set(fecha_actual.strftime("%d/%m/%Y"))
                self.hora_var.set(hora_actual.strftime("%H:%M"))
                self.descripcion_var.set("")
                self.duracion.set("1 Hora")
                self.importancia_var.set(False)

# ! ESTO TRAE TODO LA LISTA TOTAL DE LOS EVENTO NO IMPORT LOS DIA NI LAS FECHAS
# impletarlo con un text area si es que existe
    def modificar(self):
        with open("eventos.csv", newline="") as archivo:
            contenido = csv.reader(archivo)
            for row in contenido:
                self.titulo_var.set(row[1])
                self.fecha_var.set(row[2])
                self.hora_var.set(row[3])
                self.duracion.set(row[4])
                self.descripcion_var.set(row[5])
                #self.importancia_var.set(row[4]) -> No se puede asignar un valor booleano a un StringVar err=??

    def buscar_evento(self):
        buscado = self.buscar.get()
        with open("eventos.csv", newline="") as archivo:
            contenido = csv.reader(archivo)
            for row in contenido:
                titulo = row[0]
                if titulo == buscado:
                    self.titulo_var.set(row[0])
                    self.fecha_var.set(row[1])
                    self.hora_var.set(row[2])
                    self.descripcion_var.set(row[3])
                    self.duracion.set(row[4])
                    self.importancia_var.set(False)
                    return
            messagebox.showwarning("Error", "No se encontró el evento")
        
    
    def comprobar_hora(self):
        fecha_actual = self.fecha_var.get()
        hora_actual = self.hora_var.get()


        with open("eventos.csv", newline="") as archivo:
            contenido = csv.reader(archivo)
            for row in contenido:
                fecha = row[1]
                hora = row[2]

                if fecha == fecha_actual and hora == hora_actual:
                    return True

