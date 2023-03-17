import tkinter as tk
from tkinter import messagebox
import csv
import datetime as dt

class EventForm:
    id_evento = 0

    def __init__(self, root):
        self.root = root
        root.title("Formulario de eventos")

        # Definir variables de control
        self.titulo_var = tk.StringVar()
        self.fecha_var = tk.StringVar()
        self.hora_var = tk.StringVar()
        self.descripcion_var = tk.StringVar()
        self.importancia_var = tk.BooleanVar()
        #self.id_evento = self.identificador()



        # obtener la fecha y la hora actual
        fecha_actual = dt.date.today()
        self.fecha_var.set(fecha_actual.strftime("%d/%m/%Y"))

        hora_actual = dt.datetime.now().time()
        self.hora_var.set(hora_actual.strftime("%H:%M"))

        # Crear etiquetas y campos de entrada
        tk.Label(root, text="Título:").grid(row=0, column=0)
        tk.Entry(root, textvariable=self.titulo_var).grid(row=0, column=1)

        tk.Label(root, text="Fecha (DD/MM/AAAA):",).grid(row=1, column=0)
        tk.Entry(root, textvariable=self.fecha_var).grid(row=1, column=1)

        tk.Label(root, text="Hora (HH:MM):").grid(row=2, column=0)
        tk.Entry(root, textvariable=self.hora_var).grid(row=2, column=1)

        tk.Label(root, text="Descripción:").grid(row=3, column=0)
        tk.Entry(root, textvariable=self.descripcion_var).grid(row=3, column=1)

        tk.Label(root, text="Importancia:").grid(row=4, column=0)
        tk.Checkbutton(root, variable=self.importancia_var).grid(row=4, column=1)

        # Crear botones
        # tk.Button(root, text="Crear evento", command=self.crear_evento).grid(row=5, column=0)
        tk.Button(root, text="Modificar evento", command=self.buscar_evento).grid(row=5, column=1)
        tk.Button(root, text="Eliminar evento", command=self.eliminar_evento).grid(row=5, column=2)
        tk.Button(root, text="Guardar", command=self.guardar).grid(row=6, column=0)
        tk.Button(root, text="Cargar", command=self.cargar).grid(row=6, column=1)



    def eliminar_evento(self):
        # Obtener el título del evento a eliminar
        titulo = self.titulo_var.get()

        # Leer los eventos desde el archivo CSV
        eventos = []
        with open("eventos.csv", newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] != titulo:  # si el título no coincide, agregar el evento a la lista
                    eventos.append(row)

        # Escribir los eventos actualizados al archivo CSV
        with open("eventos.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(eventos)

        # Limpiar los campos de entrada
        self.titulo_var.set("")
        self.fecha_var.set("")
        self.hora_var.set("")
        self.descripcion_var.set("")
        self.importancia_var.set(False)

    def guardar(self):
        id_v = self.id_evento = self.identificador()
        import os
        import csv

        datos = [{"ID": id_v, 
                "Titulo": self.titulo_var.get(), 
                "Fecha": self.fecha_var.get(),
                "Hora": self.hora_var.get(),
                "Descripcion": self.descripcion_var.get(), 
                "Importancia": self.importancia_var.get()
                }]

        file_exists = os.path.exists("eventos.csv")
        if not file_exists:
            messagebox.showinfo("Error", "No existe el archivo")
        else:
            with open("eventos.csv", "a", newline="") as csvfile:
                campos = ["ID", "Titulo", "Fecha", "Hora", "Descripcion", "Importancia"]
                writer = csv.DictWriter(csvfile, fieldnames=campos)
                writer.writeheader()
                for data in datos:
                    writer.writerow(data)

# ! ESTO TRAE TODO LA LISTA TOTAL DE LOS EVENTO NO IMPORT LOS DIA NI LAS FECHAS
    def cargar(self):
        with open("eventos.csv", newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.titulo_var.set(row[1])
                self.fecha_var.set(row[2])
                self.hora_var.set(row[3])
                self.descripcion_var.set(row[4])
                #self.importancia_var.set(row[4]) -> No se puede asignar un valor booleano a un StringVar err=??

    def buscar_evento(self):
        buscado = self.titulo_var.get()
        with open("eventos.csv", newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == buscado:
                # traer los datos del csv que sean igual al buscado
                    pass

    @staticmethod
    def identificador():
        EventForm.id_evento += 1
        return EventForm.id_evento


