import tkinter as tk
from tkinter import ttk
from tkinter import  messagebox
from tkcalendar import Calendar
import calendar
from evento import Evento

class Calendario(ttk.Frame, Evento):
    def __init__(self, root, nombre=None, fecha=None, hora=None, duracion=1):
        super().__init__(root)
        #Evento.__init__(self, nombre, fecha, hora, duracion) # ? Preguntar como hacer sin esto por que da error en la ventana 
        self.root = root
        self.pack()
        self.crear_calendario()

    def crear_calendario(self):
        # crear un objeto Calendar de tkcalendar y mostrarlo en la ventana
        self.calendario = Calendar(self, selectmode="day", date_pattern="yyyy-mm-dd", font="Arial 20")
        self.calendario.pack(padx=10, pady=10)
        # self.root.geometry("400x400") -> no funciona 

        # agregar un boton para agregar evento
        boton_agregar = tk.Button(self, text="Agregar evento", command=self.agregar_evento)
        boton_agregar.pack(padx=10, pady=10)

    def agregar_evento(self):
        # obtener la fecha seleccionada en el calendario
        fecha_seleccionada = self.calendario.selection_get()

        # # crear un cuadro de diálogo para agregar un evento
        evento = " "

        # # mostrar un mensaje de confirmación del evento agregado
        if evento:
            messagebox.showinfo("Evento agregado", f"Se agregó el evento '{evento}' para el {fecha_seleccionada}.")

# crear la ventana principal y mostrar el calendario
ventana = tk.Tk()
calendario = Calendario(root=ventana)
calendario.mainloop()