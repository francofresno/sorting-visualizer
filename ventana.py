try:
    from tkinter import filedialog
    from tkinter import *
except ImportError:
    raise ImportError("Se requiere el modulo tkinter")
from sorting_algorithms import *
from merge_sort import *
from quick_sort import *
from bubble_sort import *
from heap_sort import *
from lista_manager import *
from functools import partial

class Ventana(ListaManager):
    ventana = Tk()
    un_archivo = None

    def __init__(self,titulo):
        self.ventana.title(titulo)
        self.canvas = Canvas(self.ventana, height=600, width=600, bg="#263D42")
        self.frame = Frame(self.ventana, bg="white")
        self.merge_sort = Button(self.ventana, text="Merge Sort", padx=10, pady=5, fg="white", bg="#263D42", command=partial(self.ordenar,Algoritmo(MergeSort())))
        self.quick_sort = Button(self.ventana, text="Quick Sort", padx=10, pady=5, fg="white", bg="#263D42", command=partial(self.ordenar,Algoritmo(QuickSort())))
        self.heap_sort = Button(self.ventana, text="Heap Sort", padx=10, pady=5, fg="white", bg="#263D42", command=partial(self.ordenar,Algoritmo(HeapSort())))
        self.bubble_sort = Button(self.ventana, text="Bubble Sort", padx=10, pady=5, fg="white", bg="#263D42", command=partial(self.ordenar,Algoritmo(BubbleSort())))
        self.selec_archivo = Button(self.ventana, text="Seleccionar Archivo", padx=10, pady=5, fg="white", bg="#FF5733", command=self.archivo_a_lista)
        
    def configurar(self):
        self.ventana.resizable(width=False, height=False)
        self.canvas.pack(fill=BOTH)
        self.frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.08)
        self.merge_sort.pack(side=LEFT)
        self.quick_sort.pack(side=LEFT)
        self.heap_sort.pack(side=LEFT)
        self.bubble_sort.pack(side=LEFT)
        self.selec_archivo.pack(side=BOTTOM , fill=BOTH)

    def iniciar(self):
        self.ventana.mainloop()

    def archivo_a_lista(self):
        self.un_archivo = filedialog.askopenfilename(initialdir='/',title="Seleccionar Archivo",filetypes=[("Textos", "*.txt")])
        if self.un_archivo is not None: 
            with open(self.un_archivo, "r") as archivo_nuevo:
                self.txt_a_lista(archivo_nuevo)

    def ordenar(self, algoritmo_a_aplicar):
        algoritmo_a_aplicar.ordenar(self)



#            Label(self.canvas, text=f.read()).pack()

