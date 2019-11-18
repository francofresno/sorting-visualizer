from sorting_algorithms import *
from lista_manager import *
try:
    from tkinter import filedialog
    from tkinter import *
except ImportError:
    raise ImportError("Se requiere el modulo tkinter")

class Ventana(ListaManager):
    ventana = Tk()
    un_archivo = None

    def __init__(self,titulo):
        self.ventana.title(titulo)
        self.canvas = Canvas(self.ventana, height=600, width=600, bg="#263D42")
        self.merge_sort = Button(self.ventana, text="Merge Sort", padx=10, pady=5, fg="white", bg="#263D42")
        self.quick_sort = Button(self.ventana, text="Quick Sort", padx=10, pady=5, fg="white", bg="#263D42")
        self.heap_sort = Button(self.ventana, text="Heap Sort", padx=10, pady=5, fg="white", bg="#263D42")
        self.bubble_sort = Button(self.ventana, text="Bubble Sort", padx=10, pady=5, fg="white", bg="#263D42")
        self.abrir_archivo = Button(self.ventana, text="Abrir Archivo", padx=10, pady=5, fg="white", bg="#FF5733", command=self.abrir_un_archivo)
        
    def configurar(self):
        self.canvas.pack(fill=BOTH)
        self.merge_sort.pack(side=LEFT)
        self.quick_sort.pack(side=LEFT)
        self.heap_sort.pack(side=LEFT)
        self.bubble_sort.pack(side=LEFT)
        self.abrir_archivo.pack(side=BOTTOM , fill=BOTH)

    def iniciar(self):
        self.ventana.mainloop()

    def abrir_un_archivo(self):
        self.un_archivo = filedialog.askopenfilename(initialdir='/',title="Seleccionar Archivo",filetypes=[("Textos", "*.txt")])
        if self.un_archivo is not None: 
            with open(self.un_archivo, "r") as archivo_nuevo:
                self.txt_a_lista(archivo_nuevo)

    def ordenar(self,algoritmo_a_aplicar):
        algoritmo_a_aplicar.ordenar(self.lista_numeros)




#            Label(self.canvas, text=f.read()).pack()

