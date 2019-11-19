from time import *

class Algoritmo:
    tiempoInicial = None
    tiempoFinal = None
    tipo_algoritmo = None
    lista_ordenada = []

    def __init__(self, tipo):
        self.tipo_algoritmo = tipo
    
    def ordenar(self, ventana):
        lista_enteros = ventana.lista_numeros
        self.tiempoInicial = time()
        self.lista_ordenada = self.tipo_algoritmo.ordenar_numeros(lista_enteros)
        self.tiempoFinal = time()
        self.imprimirResultados(ventana)
#        print("Comparaciones:", self.tipo_algoritmo.comparaciones)
#        print(self.lista_ordenada)
#        print("Tiempo: {0:f} segundos".format(self.tiempoFinal - self.tiempoInicial))
        # reset a 0 de la var comparaciones del algoritmo usado
        self.tipo_algoritmo.resetearComparaciones()

    def imprimirResultados(self,ventana):
        #ventana.permitirGuardar()
        return 0