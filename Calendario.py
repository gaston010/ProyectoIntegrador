import tkinter as tk
from tkinter import LEFT, ttk
from tkinter import  messagebox
from tkcalendar import Calendar
from evento import Evento

class Calendario(ttk.Frame, Evento):
    def __init__(self, root, nombre=None, fecha=None, hora=None, duracion=1):
        super().__init__(root)
        #Evento.__init__(self, nombre, fecha, hora, duracion) # ? Preguntar como hacer sin este por que da error en la ventana 
        self.root = root
        self.pack()
        self.crear_calendario()
        self.botones()

    def crear_calendario(self):
        # crear un objeto Calendar de tkcalendar y mostrarlo en la ventana
        self.calendario = Calendar(self, selectmode="day", date_pattern="yyyy-mm-dd", font="Arial 20")
        self.calendario.grid(row=1, column=1)
        # self.root.geometry("400x400") -> no funciona 
    
    def botones(self):
        # agregar un boton para agregar evento
        boton_agregar = tk.Button(self, text="Agregar evento", command=self.boton_evento)
        boton_agregar.grid(row=2, column=0)

        boton_modificar = tk.Button(self, text="Modificar", command=self.mod_evento)
        boton_modificar.grid(row=2, column=1)

        boton_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_evento)
        #boton_eliminar.pack(padx=10, pady=10)


    def boton_evento(self, nombre=None, fecha=None, hora=None, duracion=1):
        # obtener la fecha seleccionada en el calendario
        fecha_seleccionada = self.calendario.selection_get()

        # # crear un cuadro de diálogo para agregar un evento
        evento = ""

        # # mostrar un mensaje de confirmación del evento agregado
        if evento:
            messagebox.showinfo("Evento agregado", f"Se agregó el evento '{evento}' para el {fecha_seleccionada}.")
    
    def mod_evento(self):
        import csv
        dia_seleccionado = self.calendario.selection_get()
        #print(dia_seleccionado)
        with open('eventos.csv') as archivo:
            linea_0 = csv.reader(archivo)
            for linea in archivo:
            
                if linea[1] == dia_seleccionado:
                    print('Dia Seleccionad',linea)
                else:
                    print('No hay eventos para este dia')


    def eliminar_evento(self):
        delete = self.calendario.selection_get()
        print(delete)
        pass




# crear la ventana principal y mostrar el calendario
ventana = tk.Tk()
calendario = Calendario(root=ventana)
calendario.mainloop()