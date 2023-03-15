from csv import writer
import datetime as dt  # dt FECHA Y HORAS
import tkinter as tk
from tkinter import StringVar, ttk, messagebox

class Evento(ttk.Frame):

    id_evento =0

    def __init__(self,root):
    # def __init__(self,root, titulo, fecha, hora, descripcion= None, duracion = 1.00, importancia  = False):
        self.titulo = StringVar()
        self.fecha = StringVar() # podria cambiarse a dt.date(year, mes, dia) 
        self.hora = StringVar()
        self.descripcion = StringVar()
        self.duracion = StringVar()
        self.importancia = StringVar()
        self.id_evento = self.identificador()
        self.root = root     
        root.geometry("307x381")


        titulo=tk.Label(root)
        titulo["text"] = "Titulo del Evento"
        titulo.place(x=10,y=30,width=70,height=25)

        gettitulo=tk.Entry(root, textvariable=self.titulo)
        gettitulo.place(x=90,y=30,width=202,height=30)


        #Label y boton FECHA
        fecha=tk.Label(root)
        fecha["text"] = "Fecha"
        fecha.place(x=0,y=70,width=70,height=25)

        fecha=tk.Entry(root, textvariable=self.fecha)
        fecha_actual = dt.date.today()
        fecha.insert(0,str(fecha_actual))
        fecha.place(x=90,y=70,width=201,height=30)

  

        #Label y boton Hora
        hora=tk.Label(root)
        hora["text"] = "Hora"
        hora.place(x=0,y=110,width=70,height=25)

        hora=tk.Entry(root, textvariable=self.hora)
        hora_actual = dt.datetime.now().time()
        hora_str = hora_actual.strftime("%H:%M")
        hora.insert(0,str(hora_str))
        hora.place(x=90,y=110,width=200,height=30)


        #Label y boton Description
        descripcion=tk.Label(root)
        descripcion["text"] = "Descripcion"
        descripcion.place(x=0,y=150,width=70,height=25)
        
        descripcion=tk.Entry(root, textvariable=self.descripcion)
        descripcion.place(x=90,y=150,width=200,height=30)


        #Label y boton Duracion
        duracion=tk.Label(root)
        duracion["text"] = "Duracion"
        duracion.place(x=0,y=190,width=70,height=25)

        duracion=tk.Entry(root, textvariable=self.duracion)
        duracion.insert(0,'1') # Colocar por defecto el valor de 1 hora 
        duracion.place(x=90,y=190,width=198,height=30)
        
        #Label y boton Importancia 
        importancia=tk.Label(root)
        importancia["text"] = "Importancia"
        importancia.place(x=0,y=230,width=70,height=25)

        importancia=tk.Entry(root, textvariable=self.importancia)
        importancia.insert(0,"Si")
        importancia.place(x=90,y=230,width=199,height=30)
        

        #Boton Crear
        evento_n=tk.Button(root)
        evento_n["text"] = "Crear Evento"
        evento_n.place(x=10,y=300,width=70,height=30)
        evento_n["command"] = self.crear_nuevo
        evento_n.delete(0, tk.END) 
       
        #Boton Cancelar
        cancelar=tk.Button(root)
        cancelar["text"] = "Cancelar"
        cancelar.place(x=100,y=300,width=70,height=30)
        cancelar["command"] = self.boton_cancelar

        #Boton Modificar
        modificar=tk.Button(root)
        modificar["text"] = "Modificar Evento"
        modificar.place(x=10,y=350,width=70,height=30)
        modificar["command"] = self.modificar

        #Boton Eliminar
        # eliminar=tk.Button(root)
        # eliminar["text"] = "Eliminar Evento"
        # eliminar.place(x=100,y=350,width=70,height=30)
        # eliminar["command"] = self.eliminar

        # #Boton Guardar
        # guardar=tk.Button(root)
        # guardar["text"] = "Guardar"
        # guardar.place(x=10,y=400,width=70,height=30)
        # guardar["command"] = self.guardar


    
    def crear_nuevo(self):
        print(self.titulo.get(), self.fecha.get(), self.fecha.get(), self.descripcion.get(), self.duracion.get(), self.importancia.get())
        self.__nuevo()


    def boton_cancelar(self):
        self.root.destroy()

    def __nuevo(self):
        import csv
        import datetime as dt
        titulo = self.titulo.get()
        fecha_get = self.fecha.get()
        hora_get = self.hora.get()
        descripcion = self.descripcion.get()
        duracion = self.duracion.get()
        imp = self.importancia.get()
        id_v = self.identificador()

        if imp =='Si':
            importancia = True
        else:
            importancia = False

        fecha = dt.datetime.strptime(fecha_get, '%Y-%m-%d').date()
        hora = dt.datetime.strptime(hora_get, "%H:%M").time()
        
        # ! FALTA VALIDAR QUE LOS DATOS INGRESADOS SEAN CORRECTOS
        # ! Los encabezado no se agregan en el inicio del archivo arreglar tal problema 
        #encabezado = ['id', 'titulo', 'fecha', 'hora', 'descripcion', 'duracion', 'importancia']

        # ? el dicc no guarda median el writerow por un errr de tipo de dato
        #ev = {'id': id_v, 'titulo': titulo, 'fecha': fecha, 'hora': hora, 'descripcion': descripcion, 'duracion': duracion, 'importancia': importancia}

        
        with open('eventos.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([id_v, titulo, fecha, hora, descripcion, duracion, importancia])
        
        # ! modificar no trae la informacion del archivo
    def modificar(self):
        import csv
        with open('eventos.csv') as eventos:
            reader = csv.reader(eventos)
            lista = list(reader)
        for i in lista:
            print(i)



    @classmethod
    def identificador(cls):
        cls.id_evento += 1
        return cls.id_evento


# root = tk.Tk()
# p = Evento(root)
# root.mainloop()

