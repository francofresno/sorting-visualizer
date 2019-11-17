try:
    from tkinter import filedialog
    from tkinter import *
except ImportError:
    raise ImportError("Se requiere el modulo tkinter")

class Ventana():
    ventana = Tk()
    unArchivo = None

    def __init__(self,titulo):
        self.ventana.title(titulo)
        self.canvas = Canvas(self.ventana, height=600, width=600, bg="#263D42")
        self.mergeSort = Button(self.ventana, text="Merge Sort", padx=10, pady=5, fg="white", bg="#263D42")
        self.quickSort = Button(self.ventana, text="Quick Sort", padx=10, pady=5, fg="white", bg="#263D42")
        self.heapSort = Button(self.ventana, text="Heap Sort", padx=10, pady=5, fg="white", bg="#263D42")
        self.bubbleSort = Button(self.ventana, text="Bubble Sort", padx=10, pady=5, fg="white", bg="#263D42")
        self.abrirArchivo = Button(self.ventana, text="Abrir Archivo", padx=10, pady=5, fg="white", bg="#FF5733", command=self.abrirUnArchivo)
        
    def configurar(self):
        self.canvas.pack(fill=BOTH)
        self.mergeSort.pack(side=LEFT)
        self.quickSort.pack(side=LEFT)
        self.heapSort.pack(side=LEFT)
        self.bubbleSort.pack(side=LEFT)
        self.abrirArchivo.pack(side=BOTTOM , fill=BOTH)

    def iniciar(self):
        self.ventana.mainloop()

    def abrirUnArchivo(self):
        self.unArchivo = filedialog.askopenfilename(initialdir='/',title="Seleccionar Archivo",filetypes=[("Textos", "*.txt")])

    # if unArchivo is None ...