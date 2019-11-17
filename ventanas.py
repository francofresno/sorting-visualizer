from abc import ABC, abstractmethod
try:
    from tkinter import *
except ImportError:
    raise ImportError("Se requiere el modulo tkinter")

class Ventana(ABC):
    ventana = Tk()

    def __init__(self,titulo):
        self.ventana.title(titulo)
        self.ventana.minsize(800,600)

    @abstractmethod
    def configurar(self):
        pass

    def iniciar(self):
        self.ventana.mainloop()

class Principal(Ventana):

    def configurar(self):
        infoInput = Label(self.ventana,text="Ingrese una lista de enteros separados por ',': ")
        inputBox = Entry(self.ventana, textvariable = StringVar())
        infoInput.grid(row=1,column=1)
        inputBox.grid(row=1,column=3)