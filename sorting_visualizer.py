try:
    from tkinter import *
except ImportError:
    raise ImportError("Se requiere el modulo tkinter")

ventana = Tk()
ventana.minsize(800, 600) 
infoInput=Label(ventana,text="Ingrese una lista de enteros separados por ',': ")
infoInput.grid(row=1,column=1)
ventana.title('Sorting Visualizer')
variable_string = StringVar()
caja = Entry(ventana,textvariable=variable_string)
caja.grid(row=1,column=3)

ventana.mainloop()