import csv
from ctypes import sizeof
import datetime as dt
import os
import tkinter as tk
from tkinter import messagebox, ttk, END

import src.conexion as con

class Evento():
    id_evento = 0

    def __init__(self, root):
        self.root = root
        root.title("Formulario de eventos")
        self.root.geometry("600x500")

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
        self.fecha_var.set(fecha_actual.strftime("%Y/%m/%d"))

        hora_actual = dt.datetime.now().time()
        self.hora_var.set(hora_actual.strftime("%H:%M"))
        
        self.duracion.set("1 hora")


        # Crear etiquetas y campos de entrada
        tk.Label(root, text="Título:").grid(row=0, column=0)
        self.titu = tk.Entry(root,textvariable=self.titulo_var)
        self.titu.grid(row=0, column=1)
        self.titu.focus()
        
        tk.Label(root, text="Fecha (YY/MM/DD):",).grid(row=1, column=0)
        self.fecha=tk.Entry(root, textvariable=self.fecha_var)
        self.fecha.grid(row=1, column=1)

        tk.Label(root, text="Hora (HH:MM):").grid(row=2, column=0)
        self.hora=tk.Entry(root, textvariable=self.hora_var)
        self.hora.grid(row=2, column=1)

        tk.Label(root, text="Descripción:").grid(row=3, column=0)
        self.des=tk.Entry(root, textvariable=self.descripcion_var)
        self.des.grid(row=3, column=1)

        tk.Label(root, text="Importancia:").grid(row=5, column=0)
        self.imp= tk.Checkbutton(root, variable=self.importancia_var)
        self.imp.grid(row=5, column=1)

        tk.Label(root, text="Duracion:").grid(row=4, column=0)
        self.dur=ttk.Combobox(root, textvariable=self.duracion, values=["1 Hora", "2 Horas", "3 Horas", "4 Horas", "5 Horas", "6 Horas", "7 Horas", "8 Horas", "9 Horas", "10 Horas", "11 Horas", "12 Horas", "13 Horas", "14 Horas", "15 Horas", "16 Horas", "17 Horas", "18 Horas", "19 Horas", "20 Horas", "21 Horas", "22 Horas", "23 Horas", "24 Horas"])
        self.dur.grid(row=4, column=1)

        tk.Label(root, text="Buscar Evento:").grid(row=0, column=2)
        tk.Entry(root, textvariable=self.buscar).grid(row=0, column=3)
        
        ev=tk.Label(root, text="Eventos:", font="Arial")
        ev.grid(row=8, column=2)
        ev.config(font=("Arial", 20))

        #Genera una lista para mostrar los eventos
        self.arbol = ttk.Treeview(root, columns=("Titulo", "Fecha", "Hora", "Descripcion", "Duracion", "Importancia"))
        self.arbol.grid(row=9, column=0, columnspan=4)
        self.arbol.heading("#0", text=" ")
        self.arbol.heading("Titulo", text="Titulo")
        self.arbol.heading("Fecha", text="Fecha")
        self.arbol.heading("Hora", text="Hora")
        self.arbol.heading("Descripcion", text="Descripcion")
        self.arbol.heading("Duracion", text="Duracion")
        self.arbol.heading("Importancia", text="Importancia")
        self.arbol.column("#0", width=0)
        self.arbol.column("Titulo", width=100)
        self.arbol.column("Fecha", width=100)
        self.arbol.column("Hora", width=100)
        self.arbol.column("Descripcion", width=100)
        self.arbol.column("Duracion", width=100)
        self.arbol.column("Importancia", width=100)
        if os.path.exists("eventos.csv"):
            self.cargar_eventos()
        
        # Crear botones
        btnguardar =  tk.Button(root, text="Crear Nuevo Evento", command=self.guardar)
        btnguardar.grid(row=6, column=0)
        
        tk.Button(root, text="Modificar", command=self.modificar).grid(row=7, column=0)
        tk.Button(root, text="Eliminar evento", command=self.eliminar_evento).grid(row=6, column=2)
        tk.Button(root, text="Buscar", command=self.buscar_evento).grid(row=1, column=3)

        cerrar = tk.Button(root, text="Cerrar", command=root.destroy) 
        cerrar.grid(row=7, column=2)

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
            self.fecha_var.set(fecha_actual.strftime("%Y/%m/%d"))
            self.hora_var.set(hora_actual.strftime("%H:%M"))
            self.descripcion_var.set("")
            self.duracion.set("1 Hora")
            self.importancia_var.set(False)
            self.titu.focus()


    def guardar(self):
        import os
        import datetime

        # Verificar si el título está vacío
        if not self.titulo_var.get():
            messagebox.showwarning("Error", "El título es obligatorio")
            return

        # Verificar si el título ya existe en la base de datos
        if con.Conexion().buscar(self.titulo_var.get()):
            messagebox.showwarning("Error", "El título ya existe")
            return

        # Insertar el evento en la base de datos
        titulo = self.titulo_var.get()
        fecha = self.fecha_var.get()
        hora = self.hora_var.get()
        descripcion = self.descripcion_var.get()
        duracion = self.duracion.get()
        importancia = self.importancia_var.get()
        con.Conexion().insertar(titulo, fecha, hora, descripcion, duracion, importancia)
        messagebox.showinfo("Información", "Evento guardado correctamente")

        # Limpiar los campos de entrada
        self.titulo_var.set("")
        self.fecha_var.set(datetime.date.today().strftime("%d/%m/%Y"))
        self.hora_var.set(datetime.datetime.now().time().strftime("%H:%M"))
        self.descripcion_var.set("")
        self.duracion.set("1 Hora")
        self.importancia_var.set(False)
        self.titu.focus()
        self.arbol.update()



# impletarlo con un text area si es que existe
    #ModificarByCristian
    def modificar(self):
        titulo= self.titulo_var.get()
        fecha= self.fecha_var.get()
        hora=self.hora_var.get()
        descripcion= self.descripcion_var.get()
        duracion=self.duracion.get()
        importancia= self.importancia_var.get()
        

        pos_mod = self.buscar_evento()#Esto me devuelve la posicion del buscado
        filas=[]#aqui guardamos todo el nuevo contenido
        #trae todo en contenido y modifica la posicion obtenida en pos_mod 
        with open("eventos.csv", "r",newline="") as archivo:
            contenido = csv.reader(archivo)
            for i,fila in enumerate(contenido):
                if i==pos_mod:
                    fila= [
                            titulo,
                            fecha,
                            hora,
                            descripcion,
                            duracion,
                            importancia
                            ]
                filas.append(fila)
        #Escribe el archivo con la nueva modificacion
        with open("eventos.csv","w",newline="") as archivo:
            escritor_csv= csv.writer(archivo)
            for fila in filas:
                escritor_csv.writerow(fila)
                self.arbol.update() # actualiza el arbol

        messagebox.showinfo("Información", "Evento modificado correctamente")

    #Buscar Modificado Cristian 
    def buscar_evento(self):
            # Obtener el título del evento a buscar
            title = self.titulo_var.get()
            buscar = con.Conexion().buscar(title)
            if buscar:
                # Si se encontraron resultados, vaciar los campos antes de rellenarlos
                self.titulo_var.set("")
                self.fecha_var.set("")
                self.hora_var.set("")
                self.descripcion_var.set("")
                self.duracion.set("")
                self.importancia_var.set(False)
                # Recorrer los resultados y rellenar los campos
                for i in buscar:
                    self.titulo_var.set(str(i[0]))
                    self.fecha_var.set(str(i[1]))
                    self.hora_var.set(str(i[2]))
                    self.descripcion_var.set(str(i[3]))
                    self.duracion.set(str(i[4]))
            else:
                messagebox.showwarning("Error", "No se encontraron resultados")


    def comprobar_hora(self):
        fecha_actual = self.fecha_var.get()
        hora_actual = self.hora_var.get()
        hora = con.Conexion().buscarhora(hora_actual)
            
        if hora == hora_actual:
            for row in hora:
                if row[1] == fecha_actual:
                    return True
                else:
                    return False


    def cargar_eventos(self):
        buscar = con.Conexion().buscartodo()
        if buscar:
            for row in buscar:
                if row[5] == 1:
                    tags = ('1',)
                else:
                    tags = ()
                self.arbol.insert("", "end", values=row, tags=tags)
            self.arbol.tag_configure('1', background='green')
        self.arbol.update() # actualiza el arbol
