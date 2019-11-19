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
    archivo_ingresado = None
    archivo_resultado = None

    def __init__(self,titulo):
        self.ventana.title(titulo)
        self.canvas = Canvas(self.ventana, height=600, width=900, bg="#263D42")
        self.frame = Frame(self.ventana, bg="white")
        self.merge_sort = Button(self.ventana, text="Merge Sort", padx=10, pady=5, fg="white", bg="#263D42", command=partial(self.ordenar,Algoritmo(MergeSort())))
        self.quick_sort = Button(self.ventana, text="Quick Sort", padx=10, pady=5, fg="white", bg="#263D42", command=partial(self.ordenar,Algoritmo(QuickSort())))
        self.heap_sort = Button(self.ventana, text="Heap Sort", padx=10, pady=5, fg="white", bg="#263D42", command=partial(self.ordenar,Algoritmo(HeapSort())))
        self.bubble_sort = Button(self.ventana, text="Bubble Sort", padx=10, pady=5, fg="white", bg="#263D42", command=partial(self.ordenar,Algoritmo(BubbleSort())))
        self.selec_archivo = Button(self.ventana, text="Seleccionar Archivo", padx=10, pady=5, fg="white", bg="#FF5733", command=self.archivo_a_lista)
        self.save_archivo = Button(self.frame, text="Guardar Archivo", padx=10, pady=5, fg="white", bg="#FF5733", command=self.guardar_archivo)
        self.lista_ing_label = Label(self.frame, text="Lista ingresada:")
        self.lista_ord_label = Label(self.frame, text="Lista ordenada:")
        self.comparaciones_label = Label(self.frame, text="Comparaciones realizadas para ordenar:")
        self.tiempo_label = Label(self.frame, text="Tiempo transcurrido (se considerará 0 si es menor a 0.000001):")
        self.numeros_ingresados = Label(self.frame, text="")
        self.numeros_ordenados = Label(self.frame, text="")
        self.comp_hechas = Label(self.frame, text="")
        self.tiempo_transc = Label(self.frame, text="")

    def configurar(self):
        self.ventana.resizable(width=FALSE, height=FALSE)
        self.canvas.pack(fill=BOTH)
        self.frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.08)
        self.merge_sort.pack(side=LEFT, fill=BOTH)
        self.quick_sort.pack(side=LEFT, fill=BOTH)
        self.heap_sort.pack(side=LEFT, fill=BOTH)
        self.bubble_sort.pack(side=LEFT, fill=BOTH)
        self.selec_archivo.pack(side=BOTTOM, fill=BOTH)
        self.save_archivo.pack(side=BOTTOM, fill=BOTH)
        self.lista_ing_label.pack(side=TOP, fill=BOTH)
        self.numeros_ingresados.pack(side=TOP, fill=BOTH)
        self.lista_ord_label.pack(side=TOP, fill=BOTH)
        self.numeros_ordenados.pack(side=TOP, fill=BOTH)
        self.comparaciones_label.pack(side=TOP, fill=BOTH)
        self.comp_hechas.pack(side=TOP, fill=BOTH)
        self.tiempo_label.pack(side=TOP, fill=BOTH)
        self.tiempo_transc.pack(side=TOP, fill=BOTH)

    def iniciar(self):
        self.ventana.mainloop()

    def archivo_a_lista(self):
        self.archivo_ingresado = filedialog.askopenfilename(initialdir='/',title="Seleccionar Archivo",filetypes=[("Textos", "*.txt")])
        if self.archivo_ingresado is not None: 
            with open(self.archivo_ingresado, "r") as archivo_nuevo:
                self.txt_a_lista(archivo_nuevo)
        self.limpiarFeedbackVentana()
        if self.flag_lista_invalida:
            self.numeros_ingresados.config(text="LISTA INVÁLIDA! Ingrese otra.")
        else:
            self.numeros_ingresados.config(text=', '.join(map(str, self.lista_numeros)))

    def limpiarFeedbackVentana(self):     
        self.numeros_ordenados.config(text="")
        self.comp_hechas.config(text="")
        self.tiempo_transc.config(text="")        

    def guardar_archivo(self):
        if self.archivo_resultado is not None:
            self.archivo_resultado = filedialog.asksaveasfilename(initialdir='/',title="Guardar Archivo",filetypes=[("Textos", "*.txt")])

    def ordenar(self, algoritmo_a_aplicar):
        algoritmo_a_aplicar.ordenar(self)

    def mostrarResultados(self, algoritmo_aplicado):
        lista_ord = ', '.join(map(str, algoritmo_aplicado.lista_ordenada))
        tiempo = "{0:f} segundos".format(algoritmo_aplicado.tiempo_final - algoritmo_aplicado.tiempo_inicial)
        comparaciones_realizadas = str(algoritmo_aplicado.tipo_algoritmo.comparaciones)

        self.numeros_ordenados.config(text=lista_ord)
        self.comp_hechas.config(text=comparaciones_realizadas)
        self.tiempo_transc.config(text=tiempo)      
