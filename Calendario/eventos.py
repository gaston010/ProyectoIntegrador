import datetime as dt
import tkinter as tk
from tkinter import messagebox, ttk
import src.conexion as con
from src.data import DataRandom
import random as rd


class Evento():
    id_evento = 0

    def __init__(self, root):
        self.root = root
        root.title("Formulario de eventos")
        self.root.geometry("650x500")
        self.conexion = con.Conexion()
        self.data = DataRandom()
        con.Conexion.createdb(self.conexion)

        # Definir variables de control
        self.idEvento = tk.IntVar()
        self.titulo_var = tk.StringVar()
        self.fecha_var = tk.StringVar()
        self.hora_var = tk.StringVar()
        self.descripcion_var = tk.StringVar()
        self.duracion = tk.StringVar()
        self.importancia_var = tk.BooleanVar()

        self.buscar = tk.StringVar()
        self.buscarid = tk.StringVar()
        # self.id_evento = self.identificador() # no usado una forma mejor que no rompe las guindas # noqa

        # obtener la fecha y la hora actual
        fecha_actual = dt.date.today()
        self.fecha_var.set(fecha_actual.strftime("%Y-%m-%d"))

        hora_actual = dt.datetime.now().time()
        self.hora_var.set(hora_actual.strftime("%H:%M"))

        self.duracion.set("1 hora")

        # Crear etiquetas y campos de entrada
        tk.Label(root, text="ID:").grid(row=0, column=0)
        self.id = tk.Entry(root, textvariable=self.idEvento, state="readonly")  # noqa
        self.id.grid(row=0, column=1)

        tk.Label(root, text="Título:").grid(row=1, column=0)
        self.titu = tk.Entry(root, textvariable=self.titulo_var)
        self.titu.grid(row=1, column=1)
        self.titu.focus()

        tk.Label(root, text="Fecha (YY/MM/DD):",).grid(row=2, column=0)
        self.fecha = tk.Entry(root, textvariable=self.fecha_var)
        self.fecha.grid(row=2, column=1)

        tk.Label(root, text="Hora (HH:MM):").grid(row=3, column=0)
        self.hora = tk.Entry(root, textvariable=self.hora_var)
        self.hora.grid(row=3, column=1)

        tk.Label(root, text="Descripción:").grid(row=4, column=0)
        self.des = tk.Entry(root, textvariable=self.descripcion_var)
        self.des.grid(row=4, column=1)

        tk.Label(root, text="Importancia:").grid(row=6, column=0)
        self.imp = tk.Checkbutton(root, variable=self.importancia_var)
        self.imp.grid(row=6, column=1)

        tk.Label(root, text="Duracion:").grid(row=5, column=0)
        self.dur = ttk.Combobox(root, textvariable=self.duracion)
        self.dur.grid(row=5, column=1)

        tk.Button(root, text="Buscar Evento por Nombre:",
                  command=self.buscar_evento).grid(row=0, column=2)
        tk.Entry(root, textvariable=self.buscar).grid(row=0, column=3)

        tk.Button(root, text="Buscar por ID", command=self.buscar_evento).grid(row=1, column=2)  # noqa
        tk.Entry(root, textvariable=self.buscarid).grid(row=1, column=3)

        tk.Button(root, text="Random Data",
                  command=self.generar).grid(row=2, column=3)

        ev = tk.Label(root, text="Eventos:", font="Arial")
        ev.grid(row=8, column=2)
        ev.config(font=("Arial", 20))

        # Genera una lista para mostrar los eventos
        self.arbol = ttk.Treeview(root, columns=(
            "ID",
            "Titulo",
            "Fecha",
            "Hora",
            "Descripcion",
            "Duracion",
            "Importancia"
        ))

        self.arbol.grid(row=9, column=0, columnspan=4)
        self.arbol.heading("#0", text=" ")
        self.arbol.heading("ID", text="ID")
        self.arbol.heading("Titulo", text="Titulo")
        self.arbol.heading("Fecha", text="Fecha")
        self.arbol.heading("Hora", text="Hora")
        self.arbol.heading("Descripcion", text="Descripcion")
        self.arbol.heading("Duracion", text="Duracion")
        self.arbol.heading("Importancia", text="Importancia")
        self.arbol.column("#0", width=0)
        self.arbol.column("ID", width=10)
        self.arbol.column("Titulo", width=100)
        self.arbol.column("Fecha", width=100)
        self.arbol.column("Hora", width=100)
        self.arbol.column("Descripcion", width=100)
        self.arbol.column("Duracion", width=100)
        self.arbol.column("Importancia", width=100)
        if self.conexion:
            self.conexion.buscartodo()
            self.cargar_eventos()

        # Crear botones
        btnguardar = tk.Button(
            root, text="Crear Nuevo Evento", command=self.guardar)
        btnguardar.grid(row=6, column=0)

        tk.Button(root, text="Modificar",
                  command=self.modificar).grid(row=7, column=0)
        tk.Button(root, text="Eliminar evento",
                  command=self.eliminar_evento).grid(row=6, column=2)
        # tk.Button(root, text="Buscar", command=self.buscar_evento).grid(
        #     row=1, column=3)

        cerrar = tk.Button(root, text="Cerrar", command=root.destroy)
        cerrar.grid(row=7, column=2)

    def eliminar_evento(self):
        # Obtener el título del evento a eliminar
        if not self.titulo_var.get():
            messagebox.showwarning("Error", "El título es obligatorio")
            return

        self.conexion.eliminar(self.titulo_var.get())
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
        self.cargar_eventos()

    def generar(self):
        print("Generando datos aleatorios desde la clase data ...")
        self.data.generate_data()
        item = self.data.data
        print(item)
        for data in item:
            self.conexion.insertar(data[0], data[1], data[2],
                                   data[3], data[4], rd.choice([True, False]))
        # use for test [rmv]
        # print(rd)
        self.cargar_eventos()

    def guardar(self):
        """
        Saves an event to the database.

        Verifies if the title is empty and if it already exists in the database.
        Inserts the event into the database and displays a success message.
        Clears the input fields and focuses on the title field.
        """
        import datetime

        # Verificar si el título está vacío
        if not self.titulo_var.get():
            messagebox.showwarning("Error", "El título es obligatorio")
            return

        # Verificar si el título ya existe en la base de datos
        if self.conexion.buscar(self.titulo_var.get()):
            messagebox.showwarning("Error", "El título ya existe")
            return

        # Insertar el evento en la base de datos
        titulo = self.titulo_var.get()
        fecha = self.fecha_var.get()
        hora = self.hora_var.get()
        descripcion = self.descripcion_var.get()
        duracion = self.duracion.get()
        importancia = self.importancia_var.get()
        self.conexion.insertar(titulo, fecha, hora,
                               descripcion, duracion, importancia)
        messagebox.showinfo("Información", "Evento guardado correctamente")

        # Limpiar los campos de entrada
        self.titulo_var.set("")
        self.fecha_var.set(datetime.date.today().strftime("%d/%m/%Y"))
        self.hora_var.set(datetime.datetime.now().time().strftime("%H:%M"))
        self.descripcion_var.set("")
        self.duracion.set("1 Hora")
        self.importancia_var.set(False)
        self.titu.focus()
        self.cargar_eventos()

    def modificar(self):
        # Obtener los valores de los campos de entrada
        if not self.titulo_var.get():
            messagebox.showwarning("Error", "El título es obligatorio")
            return
        # Actualizar el evento en la base de datos
        if self.conexion.actualizar(self.titulo_var.get(
        ), self.descripcion_var.get(), self.duracion.get(), self.idEvento.get()):
            messagebox.showinfo(
                "Información", "Evento actualizado correctamente")

        self.cargar_eventos()

# Buscar por ahora funciona 26/03/2023 00:50
    def buscar_eventoid(self):
        if not self.buscarid.get():
            messagebox.showwarning("Error", "El id es obligatorio")
            return
        buscarid = self.conexion.buscarid(self.buscarid.get())
        if buscarid:
            # Si se encontraron resultados, vaciar los campos antes de rellenarlos # noqa
            self.idEvento.set("")
            self.titulo_var.set("")
            self.fecha_var.set("")
            self.hora_var.set("")
            self.descripcion_var.set("")
            self.duracion.set("")
            self.importancia_var.set(False)
            # Recorrer los resultados y rellenar los campos
            for data in buscarid:
                # cambia todo los valors a str por que no se puede escribir en el entry # noqa
                # no entender por que =¡
                self.idEvento.set(str(data[0]))
                self.titulo_var.set(str(data[1]))
                self.fecha_var.set(str(data[2]))
                self.hora_var.set(str(data[3]))
                self.descripcion_var.set(str(data[4]))
                self.duracion.set(str(data[5]))
                self.importancia_var.set(data[6])
        else:
            messagebox.showwarning("Error", "No se encontraron resultados")

    def buscar_evento(self):
        # Depurar la consulta SQL
        if not self.buscar.get():
            messagebox.showwarning("Error", "El título es obligatorio")
            return
        buscar = self.conexion.buscar(self.buscar.get())
        if buscar:
            # Si se encontraron resultados, vaciar los campos antes de rellenarlos # noqa
            self.idEvento.set("")
            self.titulo_var.set("")
            self.fecha_var.set("")
            self.hora_var.set("")
            self.descripcion_var.set("")
            self.duracion.set("")
            self.importancia_var.set(False)
            # Recorrer los resultados y rellenar los campos
            for data in buscar:
                # cambia todo los valors a str por que no se puede escribir en el entry # noqa
                # no entender por que =¡
                # TODO: Buscar mas info
                self.idEvento.set(str(data[0]))
                self.titulo_var.set(str(data[1]))
                self.fecha_var.set(str(data[2]))
                self.hora_var.set(str(data[3]))
                self.descripcion_var.set(str(data[4]))
                self.duracion.set(str(data[5]))
                # Cambia los valores a booleano para poder escribirlos en el checkbox # noqa
                self.importancia_var.set(bool(data[6]))
        else:
            messagebox.showwarning("Error", "No se encontraron resultados")
        self.arbol.update()
        self.conexion.buscartodo()

    def comprobar_hora(self):
        fecha_actual = self.fecha_var.get()
        hora_actual = self.hora_var.get()
        hora = self.conexion.buscarhora(hora_actual)

        if hora == hora_actual:
            for row in hora:
                if row[1] == fecha_actual:
                    return True
                else:
                    return False

    def cambiar_color_fondo(self, item, color):
        """
        Cambia el color de fondo del elemento especificado.

        Args:
            item (str): El identificador del elemento.
            color (str): El color de fondo.
        """
        self.arbol.tag_configure(item, background=color)

# Cargar eventos en el Treeview
# contiene algo que no genera el color sobre importancia es = 1 para darle un color # noqa
    def cargar_eventos(self):
        """
        Carga los eventos en el Treeview.

        Si hay eventos en el Treeview, los elimina antes de cargar los nuevos.
        Si el evento tiene importancia, se le asigna un color de fondo verde.
        """
        if len(self.arbol.get_children()) > 0:
            self.arbol.delete(*self.arbol.get_children())
        for _ in self.conexion.buscartodo():
            if _[6] in self.conexion.buscartodo():
                tags = ('1',)
            else:
                tags = ()
            self.arbol.tag_configure('1', background='blue')
            self.arbol.insert("", "end", values=_, tags=tags)
            self.arbol.update()
