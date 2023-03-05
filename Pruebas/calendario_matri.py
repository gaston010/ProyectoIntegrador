import tkinter as tk
import calendar
"""
    https://stackoverflow.com/questions/32289175/list-of-all-tkinter-events
    eventos del mouse y otras teclas
"""
def obtener_dias_mes(año:int, mes:int)-> int:
    """
     Obtiene los dias del mes y el año que se le pasa como parametro 
        mediante la funcion monthrange de la libreria calendar cual recorre el mes y año
        para obtener los dias del mes X

    Args:
        a (_int_): anio que quiere mostrar
        mes (_int_): mes a mostrar del respectivo año

    Returns:
        int: retorna el numero de dias del mes
    """    
    return calendar.monthrange(año, mes)[1]

def obtener_dia_semana(año, mes):
    return calendar.weekday(año, mes, 1)



class Calendario(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Calendario")
        self.pack()
       # self.__crear_calendario()


        boton_mes = tk.Button(self, text="Mes", command=self.cambiar_mes)
        boton_mes.grid(row=0, column=0)

        boton_dia = tk.Button(self, text="Dia", command=self.cambiar_dia)
        boton_dia.grid(row=0, column=1)

        boton_semana = tk.Button(self, text="Semana", command=self.cambiar_semana)
        boton_semana.grid(row=0, column=2)


    def cambiar_mes(self):
        """ 
        Agrega un boton en la interface con la funcion de mostrar el calendario del mes
        """        
        self.__crear_calendario()

    def cambiar_dia(self):

        """
        Agrega un boton en la interface con la funcion de mostrar el dia actual
        """        
        self.__crear_calendario()

    def cambiar_semana(self):
        """
        Agrega un boton en la interface con la funcion de mostrar la semana actual y los dias de la semana

        """        
        self.__crear_semana()



    def __crear_semana(self):
        self.root.geometry("600x100")

        # obtener los dias de la semana
        año = 2023 # ejemplo
        mes = 3 # ejemplo
       # dia_semana = obtener_dia_semana(año, mes)

        # crear una matriz para los días de la semana
        matriz = [[0]*7 for i in range(1)]

        dia = 1
        for columna in range(7):
            if dia <= 7:
                matriz[0][columna] = dia
                dia += 1
        
        # crear etiquetas para cada día en la matriz y mostrarlos en la ventana
        for columna in range(7):
            dia = matriz[0][columna]
            if dia != 0:
                etiqueta = tk.Label(self, text=dia, width=10, height=5)
                etiqueta.grid(row=1, column=columna)


    def __crear_calendario(self):
        """Esta función crea un calendario en una matriz de 6x7 y lo muestra en la ventana principal.

        Args:
            self (tk.Frame): la ventana principal
            obtener_dias_mes (funcion): la funcion que obtiene los dias del mes

        Returns:
            una matriz de 6x7 con los días del mes en un label cual cada label puede ser cambiado de color 
            mediante evento o bien mostrar el dia y mes en la ventana principal como title de la ventana
        """        
        self.root.geometry("800x600")
        # obtener el número de días en el mes
        año = 2023 # ejemplo
        mes = 3 # ejemplo
        dias_mes = obtener_dias_mes(año, mes)

        # crear una matriz para los días del mes
        matriz = [[0]*7 for i in range(6)]

        # llenar la matriz con los días del mes
        dia = 1
        for fila in range(6):
            for columna in range(7):
                if dia <= dias_mes:
                    matriz[fila][columna] = dia
                    dia += 1

        # crear etiquetas para cada día en la matriz y mostrarlos en la ventana
        for fila in range(6):
            for columna in range(7):
                dia = matriz[fila][columna]
                if dia != 0:
                    etiqueta = tk.Label(self, text=dia, width=8, height=4) # en cada text agrega el dia tomado de la funcion obtener_dias_mes
                    etiqueta.grid(row=fila+1, column=columna, padx=5, pady=5) # en cada grid agrega el dia tomado de la funcion obtener_dias_mes
                    """
                        [1, 2, 3, 4, 5, 6, 7],
                        [8, 9, 10, 11, 12, 13, 14],
                        [15, 16, 17, 18, 19, 20, 21],
                        [22, 23, 24, 25, 26, 27, 28],
                        [29, 30, 31, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]  
                         
                     """                    
                    # agregar eventos a las etiquetas el evento hace que cuando pase el mouse sobre ellas se muestre el día en su respectiva funcion mostrar_dia
                    etiqueta.bind("<Enter>", self.mostrar_dia)
                    # cuando realizamos click DERECHO sobre el día se cambia de color con la funcion cambiar_color
                    etiqueta.bind("<Button-1>", self.cambiar_color)
                    # al reves que el anterior ahora con el click izquierdo tornamos a color gris
                    etiqueta.bind("<Button-3>", self.cambiar_color_2)
                    #doble click agregar evento
                    etiqueta.bind("<Double-Button-1>", self.crear_evento)

                   
    
    def mostrar_dia(self, evento):
        # obtener el día que se seleccionó
        di = evento.widget.cget("text")
        dia = "Día: " + str(di) +" Mes: Marzo Año: 2023"
        # mostrar el día en la ventana principal
        self.root.title(dia)


    # esto se tiene que agregar con la clase evento para fusionarse
    def cambiar_color(self, evento):
        """
        Cambia el color de fondo de la etiqueta que se seleccionó para indicar que dicho dia tiene un evento importante

        Args:
            evento (_event_widget_): el evento que se ejecuta al hacer click izquierdo sobre la etiqueta(label) DIA
        """        
        etiqueta = evento.widget
        etiqueta.configure(bg="red")
    
    # esto se tiene que agregar con la clase evento para fusionarse
    def cambiar_color_2(self, evento):
        """
        Cambia el color de fondo de la etiqueta que se seleccionó para indicar que dicho dia tiene un evento

        Args:
            evento (_event_widget_): el evento que se ejecuta al hacer click derecho sobre la etiqueta(label) DIA
        """        
        etiqueta = evento.widget
        etiqueta.configure(bg="grey")
    

    # aun no funciona
    def crear_evento(self, evento):
        """
        Crea un evento en el dia seleccionado abriendo una nueva ventana para rellenar los datos del evento y en caso de aver un evento en el mismo dia
        preguntar si quiere modificar o bien agregar un nuevo evento en el mismo dia

        Args:
            evento (_type_): _description_
        """        
        etiqueta = evento.widget
        etiqueta.configure(bg="green")
        etiqueta.configure(text="Evento")

# crear la ventana principal y mostrar el calendario
ventana = tk.Tk()
calendario = Calendario(root=ventana)
calendario.mainloop()