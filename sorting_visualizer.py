try:
    from tkinter import *
except ImportError:
    raise ImportError("Se requiere el modulo tkinter")
""" from sorting_algorithms import *
 """
class Ventana:
    ventana = Tk()
    infoInput = Label(ventana,text="Ingrese una lista de enteros separados por ',': ")
    inputBox = Entry(ventana, textvariable = StringVar())

    def configurar(self):
        self.ventana.minsize(800,600)
        self.ventana.title('Sorting Visualizer')
        self.infoInput.grid(row=1,column=1)
        self.inputBox.grid(row=1,column=3)

    def iniciar(self):
        self.ventana.mainloop()

def main():
    print ("Hello World!")
"""     ventanaPrincipal = Ventana()
    ventanaPrincipal.configurar()
    ventanaPrincipal.iniciar() """

if __name__== "__main__":
  main()