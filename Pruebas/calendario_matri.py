import tkinter as tk
import calendar

def obtener_dias_mes(año, mes):
    return calendar.monthrange(año, mes)[1]

class Calendario(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.pack()
        self.crear_calendario()

    def crear_calendario(self):
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
                    etiqueta = tk.Label(self, text=dia, width=4, height=2)
                    etiqueta.grid(row=fila+1, column=columna, padx=5, pady=5)

# crear la ventana principal y mostrar el calendario
ventana = tk.Tk()
calendario = Calendario(root=ventana)
calendario.mainloop()
