import tkinter
from tkinter import Canvas, BOTH, Button, YES, Tk
# Creación de ventana
window = Tk()
# Tamaño y titulo de la ventana
window.title('SQL Dura Search')
window.geometry("1400x600+10+20")
# Color de la ventana
canvas = Canvas(width=1400, height=600, bg='chartreuse4')
canvas.pack(expand=YES, fill=BOTH)
canvas.create_line(10, 10, 80, 80)
canvas.create_line(10, 80, 80, 10)
# Ventana que muestra resultados
entry = tkinter.Entry()
entry.place(x=900, y=50, width=400, height=500)
# Botones
btn1 = Button(window, text="Pedidos recibidos", fg='blue')
btn1.place(x=10, y=10)
btn2 = Button(window, text="Envios realizados", fg='blue')
btn2.place(x=10, y=40)
btn3 = Button(window, text="Facturación hasta hoy", fg='blue')
btn3.place(x=10, y=70)
btn4 = Button(window, text="Facturación posible", fg='blue')
btn4.place(x=10, y=100)
btn5 = Button(window, text="Clientes nuevos", fg='blue')
btn5.place(x=10, y=130)
btn6 = Button(window, text="Pedidos de compra", fg='blue')
btn6.place(x=10, y=160)
btn7 = Button(window, text="Pedidos de compra facturación", fg='blue')
btn7.place(x=10, y=190)
btn8 = Button(window, text="Productos planificados a fabricar", fg='blue')
btn8.place(x=10, y=220)
btn9 = Button(window, text="Planificación de los reactores", fg='blue')
btn9.place(x=10, y=250)
btn10 = Button(window, text="Ordenes de producción", fg='blue')
btn10.place(x=10, y=280)
btn11 = Button(window, text="Coste ordenes de producción", fg='blue')
btn11.place(x=10, y=280)
btn12 = Button(window, text="Productos planificados a fabricar", fg='blue')
btn12.place(x=10, y=310)
btn13 = Button(window, text="Cobros que vendran este mes", fg='blue')
btn13.place(x=10, y=340)
btn14 = Button(window, text="Pagos que vendran este mes", fg='blue')
btn14.place(x=10, y=370)


def buscar_datos(dato):

    # SELECT * FROM MIDATABASE
    # donde miconexion es mi objeto de la clase Conexion
    buscar = True
    if buscar:
        for valores in buscar:
            print(valores)
            entry.insert(0, valores)


window.mainloop()
