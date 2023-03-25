# Author: Karen Gutierrez
# cambios: StringVar() , self.anio.get() <- to int(self.anio.get()) para ser operable

import tkinter as tk
from tkinter import Tk, Toplevel, ttk
import calendar

from datetime import date

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(20))
        self.parent = parent

        bu = ttk.Button(self.parent, text="Abrir Ventana", command=self.abrir_ventana)
        bu.grid(row=8, column=3)


        self.parent.title("Calendario de Eventos")
        self.parent.geometry("400x400")

        self.mes = tk.StringVar()   #se utiliza para mostrar el mes actual en un widget Label.
        self.anio = tk.StringVar()
        self.current_month = 1     #se utilizan para realizar un seguimiento del mes y año actual que se muestran en el widget Label.
        self.current_year = 2022
        self.month_name = calendar.month_name[self.current_month]
        self.days_name = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]
        self.create_calendar() #obtiene los días del mes actual y crear Labels para cada día del mes.
    
        
        # Crear botones para avanzar y retroceder un mes
        self.prev_button = ttk.Button(self.parent, text="Anterior", command=self.retrocederMes)
        #self.prev_button.pack(side=tk.LEFT)
        self.prev_button.grid(row=0,column=0)
        self.next_button = ttk.Button(self.parent, text="Siguiente", command=self.avanzarMes)
        #self.next_button.pack(side=tk.RIGHT)
        self.next_button.grid(row=0,column=5)

        mes= date.today().month
        anio= date.today().year

    def printMesAnio(self): # esto lo podes hacer con un diccionario y un for para que sea mas facil
        if self.mes==1:
            writtenMonth="Enero"
        elif self.mes==2:
            writtenMonth="Febrero"
        elif self.mes==3:
            writtenMonth="Marzo"
        elif self.mes==4:
            writtenMonth="Abril"
        elif self.mes==5:
            writtenMonth="Mayo"
        elif self.mes==6:
            writtenMonth="Junio"
        elif self.mes==7:
            writtenMonth="Julio"
        elif self.mes==8:
            writtenMonth="Agosto"
        elif self.mes==9:
            writtenMonth="Septiembre"
        elif self.mes==10:
            writtenMonth="Octubre"
        elif self.mes==11:
            writtenMonth="Noviembre"
        else:
            writtenMonth="Diciembre"

        MesAnio= ttk.Label(self.parent,text=writtenMonth +" "+str(self.anio),font= ("Arial",20))
        MesAnio.grid(column=2,row=0,columnspan=3)

    def retrocederMes(self):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        #self.cambio_mes()   # <- no la tiens defina en nigun lado no se que hace

    def avanzarMes(self):
        # Avanzar un mes
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        # Actualizar el mes mostrado
        #self.cambio_mes() # <- no la tiens defina en nigun lado no se que hace 


    def create_calendar(self):

        # Crear Label para mostrar el nombre del mes
        mesLabel= ttk.Label(self.parent, text=self.month_name) #se establece en el nombre del mes actual y la variable
        mesLabel.grid(row=0,column=0,columnspan=7)

        # Crear Label para mostrar los nombres de los días
        for i , day in enumerate(self.days_name):#es una lista de los nombres de los días de la semana.
            dayLabel= ttk.Label(self.parent, text=day, font=("Arial",14,"bold"))
            dayLabel.grid(row=1,column=i)
        #creamos tres Labels: uno para mostrar el nombre del mes actual y dos para mostrar los nombres de los días de la semana.
        
        # Obtener los días del mes actual
        mes_dias=calendar.monthcalendar(self.current_year,self.current_month)

        # Crear Labels para mostrar los días del mes actual
        for i, week in enumerate(mes_dias):
            for j,day in enumerate(week):
                if day == 0:
                    dayLabel=ttk.Label(self.parent,text="")
                else:
                    dayLabel=ttk.Label(self.parent,text=str(day),font=("Arial",14))
                    dayLabel.grid(row=i+2,column=j)

    def abrir_ventana(self):
        # creamos la ventana secundaria
        # como padre indicamos la ventana principal
        self.ventana = Toplevel(self.parent)
        SecondaryGUI(self.ventana)
    
        
    def comienzoDiaMes(self):
        ultimoDosAnios = int(self.anio.get()) - 2000 # <- Pasado a entero por que self.anio.get() es un string y no se puede operar con strings
        calcular  = ultimoDosAnios //4
        calcular += 1
        if self.mes==1 or self.mes ==10:
            calcular +=1
        elif self.mes==2 or self.mes==3 or self.mes==11:
            calcular+=4
        elif self.mes==5:
            calcular+=2
        elif self.mes==6:
            calcular+=5
        elif self.mes==8:
            calcular+=3
        elif self.mes ==9 or self.mes==12:
            calcular+=6
        else:
            calcular+=0
        anioBisiesto=self.esAnioBisiesto()
        if anioBisiesto and (self.mes ==1 or self.mes==2):
            calcular-=1
        calcular +=6
        calcular += ultimoDosAnios
        diaDeLaSemana=calcular % 7
        return diaDeLaSemana

    def diasEnMes(self):
        if self.mes==1 or self.mes==3 or self.mes==5 or self.mes==7 or self.mes==8 or self.mes==12 or self.mes ==10:
            numeroDeDias=31
        elif self.mes==4 or self.mes==6 or self.mes==9 or self.mes==11:
            numeroDeDias=30
        else:
            anioBisiesto=self.esAnioBisiesto() # <- estas pasando un parametro que no existe
            if anioBisiesto:
                numeroDeDias=29
            else:
                numeroDeDias=28
        return numeroDeDias
    
    def esAnioBisiesto(self): # <- estas pasando un parametro que no existe 
        an = int(self.anio.get()) # <- Pasado a entero por que self.anio.get() es un string y no se puede operar con strings
        """Devuelve True si year es un año bisiesto, False de lo contrario"""
        if an % 4 ==0 and(an % 100 != 0 or an % 400 == 0):
            return True
        else:
            return False
        
class SecondaryGUI:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Ventana secundaria")
        self.parent.geometry("400x400")

        # ATRIBUTOS DE LA VENTANA
        self.nombre = tk.StringVar()
        self.fecha = tk.StringVar()
        self.hora = tk.StringVar()
        self.des = tk.StringVar()
        self.imp = tk.BooleanVar()

        

        nombre = ttk.Label(self.parent, text="Nombre")
        nombre.grid(column=0, row=0)
        ennombre = ttk.Entry(self.parent, textvariable=self.nombre)
        ennombre.grid(column=1, row=0)

        fecha = ttk.Label(self.parent, text="Fecha")
        fecha.grid(column=0, row=1)
        enfec = ttk.Entry(self.parent, textvariable=self.fecha)
        enfec.grid(column=1, row=1)

        hora = ttk.Label(self.parent, text="Hora")
        hora.grid(column=0, row=2)
        enhora = ttk.Entry(self.parent, textvariable=self.hora)
        enhora.grid(column=1, row=2)

        des = ttk.Label(self.parent, text="Descripcion")
        des.grid(column=0, row=3)
        endes = ttk.Entry(self.parent, textvariable=self.des)
        endes.grid(column=1, row=3)

        imp = ttk.Label(self.parent, text="Importancia")
        imp.grid(column=0, row=4)
        enimp = ttk.Checkbutton(self.parent, textvariable=self.imp)
        enimp.grid(column=1, row=4)


        # BOTONES
        btn = ttk.Button(self.parent, text="Guardar", command=self.guardar)
        btn.grid(column=0, row=5)

        btn = ttk.Button(self.parent, text="Modificar", command=self.modificar)
        btn.grid(column=1, row=5)

        bnt = ttk.Button(self.parent, text="Eliminar", command=self.eliminar)
        bnt.grid(column=2, row=5)

        btn2 = ttk.Button(self.parent, text="Salir", command=self.salir)
        btn2.grid(column=3, row=5)

    # METODOS DE LA VENTANA
    def guardar(self):
        print("Nombre: ", self.nombre.get())
        print("Fecha: ", self.fecha.get())
        print("Hora: ", self.hora.get())
        print("Descripcion: ", self.des.get())
        print("Importancia: ", self.imp.get())
    
    def modificar(self): 
        print("Nombre: ", self.nombre.get())
        print("Fecha: ", self.fecha.get())
        print("Hora: ", self.hora.get())
        print("Descripcion: ", self.des.get())
        print("Importancia: ", self.imp.get())
    
    def eliminar(self):
        print("Nombre: ", self.nombre.get())
        print("Fecha: ", self.fecha.get())
        print("Hora: ", self.hora.get())
        print("Descripcion: ", self.des.get())
        print("Importancia: ", self.imp.get())

    def salir(self):
        self.parent.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()