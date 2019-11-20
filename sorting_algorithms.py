from time import *

class Algoritmo:
    tiempo_inicial = None
    tiempo_final = None
    tipo_algoritmo = None
    lista_ordenada = []

    def __init__(self, tipo):
        self.tipo_algoritmo = tipo
    
    def ordenar(self, ventana):
        lista_enteros = ventana.lista_numeros.copy()
        self.tiempo_inicial = time()
        self.lista_ordenada = self.tipo_algoritmo.ordenar_numeros(lista_enteros)
        self.tiempo_final = time()
        if self.lista_ordenada:
            ventana.mostrarResultados(self)
        # reset a 0 de la var comparaciones del algoritmo usado
        self.tipo_algoritmo.resetearComparaciones()