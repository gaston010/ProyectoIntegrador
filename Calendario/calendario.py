import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import calendar
from eventos import Evento



class Calendario(tk.Frame, Evento):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Calendario")
        self.root.geometry("800x600")
        #self.root.resizable(False, False)

        # obtener el mes y el año actual
        self.año_actual = 2023 # ejemplo
        self.mes_actual = 3 # ejemplo
        self.dia_semana, self.dias_mes = calendar.monthrange(self.año_actual, self.mes_actual)
        self.mes()


    def mostrar_mes(self):
        # mostrar el mes en la ventana principal
        self.root.title(calendar.month_name[self.mes_actual] + " " + str(self.año_actual))
        boton = tk.Button(self.root, text="Mes", command=self.mes)
        boton.grid(row=3, column=4)

    def mes(self):  
        # crea  etiquetas para los días de la semana 
        # ! NO CAMBIAR O MODIFICAR ESTO caso de cambiar fijarse bien en el grid y el dia de la semana se movera x+-1
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        # ? bg usa un color hexadecimal para dar mejor tonalidad y no estar tan blanco y no muy gris :(xD)
        
        # ? Fira Code una fuente personalizada para que se vea mas bonito y no tan feo en caso de no tener ninguna fuente segun su documentacion de tkinter toma la defult del sistema


        for i, dia in enumerate(dias_semana):
            etiqueta = tk.Label(self.root, text=dia, font=("Fira Code", 12), width=10, height=2, bg="#fff", bd=1, relief="solid")
            etiqueta.grid(row=0, column=i, padx=2, pady=2)

            et_dia = tk.Label(self.root)
            et_dia.bind("<Enter>", self.mostrar_dia) #ESTO SOLO MUESTRA LOS NOMBRES NO AGARRA EL DIA EN SI
            
        # crear etiquetas para cada día del mes y mostrarlos en la ventana
        fila = 1
        columna = self.dia_semana
        for dia in range(1, self.dias_mes + 1):
            etiqueta = tk.Label(self.root, text=dia, font=("Arial", 12), width=10, height=5, bg="#eee", bd=1, relief="solid")
            etiqueta.grid(row=fila+2, column=columna, padx=2, pady=2)
            columna += 1
            if columna > 6:
                fila += 1
                columna = 0

            etiqueta.bind("<Enter>", self.mostrar_dia)

            etiqueta.bind("<Button-1>", self.color_importante)
            etiqueta.bind("<Double-Button-1>", self.crear_evento)


    def consola_prueba(self, evento):
        self.root.title("prueba")

    def mostrar_dia(self, evento):
        # obtener el día que se seleccionó
        di = evento.widget.cget("text")
        dia = "Día: " + str(di) +" Mes: Marzo Año: 2023"
        # mostrar el día en la ventana principal
        self.root.title(dia)
    
    def color_importante(self, evento):
        """
        Cambia el color de fondo de la etiqueta que se seleccionó para indicar que dicho dia tiene un evento importante

        Args:
                evento (_event_widget_): el evento que se ejecuta al hacer click izquierdo sobre la etiqueta(label) DIA
        """        
        etiqueta = evento.widget
        etiqueta.configure(bg="red")
    

    def crear_evento(self, evento):
        """
        Crea un evento en el dia seleccionado abriendo una nueva ventana para rellenar los datos del evento y en caso de aver un evento en el mismo dia
        preguntar si quiere modificar o bien agregar un nuevo evento en el mismo dia

        Args:
                evento (_type_): _description_
        """        
        etiqueta = evento.widget
        etiqueta.configure(bg="green")
        if etiqueta.bind("<Double-Button-1>"):
            ventan_n = tk.Toplevel(self.root)
            Evento(ventan_n)




if __name__ == "__main__":
    p = ThemedTk(theme="blue") # no funciona :(
    calendario = Calendario(p)
    calendario.mainloop()



# # instancia  de clase
# p = tk.Tk()
# calendario = Calendario(p)
# calendario.mainloop()
