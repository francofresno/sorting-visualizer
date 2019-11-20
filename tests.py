import unittest
from ventana import *
from sorting_algorithms import *
from merge_sort import *
from heap_sort import *
from bubble_sort import *
from quick_sort import *

class TestListasIngresadas(unittest.TestCase):
    ventana = Ventana('Testing')
    lista_erronea = [["-1","4","26","a"],["0","-2"],["4"]]
    lista_valida = [["-1","4","26","985"],["0","-2"],["4"]]

    def test_lista_es_aplanada(self):
        self.assertEqual(["-1","4","26","985","0","-2","4"], self.ventana.aplanar_lista(self.lista_valida))
    
    def test_lista_es_rechazada(self):
        lista_aplanada = self.ventana.aplanar_lista(self.lista_erronea)
        self.assertRaises(ValueError, self.ventana.convertir_a_lista_de_ints, lista_aplanada)
    
    def test_lista_es_aceptada(self):
        lista_aplanada = self.ventana.aplanar_lista(self.lista_valida)
        self.ventana.convertir_a_lista_de_ints(lista_aplanada)
        self.assertEqual(False, self.ventana.flag_lista_invalida)

class TestAlgoritmos(unittest.TestCase):
    ventana = Ventana('Testing')
    ventana.lista_numeros = [33,-4,0,839,51,-1]
    lista_ordenada = [-4,-1,0,33,51,839]

    def test_merge_sort(self):
        # El algoritmo merge sort ordena correctamente la lista que cargo un usuario
        algoritmo_merge =  Algoritmo(MergeSort())
        algoritmo_merge.ordenar(self.ventana)
        self.assertEqual(self.lista_ordenada, algoritmo_merge.lista_ordenada)

    def test_quick_sort(self):
        # El algoritmo quick sort ordena correctamente la lista que cargo un usuario
        algoritmo_merge =  Algoritmo(QuickSort())
        algoritmo_merge.ordenar(self.ventana)
        self.assertEqual(self.lista_ordenada, algoritmo_merge.lista_ordenada)

    def test_heap_sort(self):
        # El algoritmo heap sort ordena correctamente la lista que cargo un usuario
        algoritmo_merge =  Algoritmo(HeapSort())
        algoritmo_merge.ordenar(self.ventana)
        self.assertEqual(self.lista_ordenada, algoritmo_merge.lista_ordenada)

    def test_bubble_sort(self):
        # El algoritmo bubble sort ordena correctamente la lista que cargo un usuario
        algoritmo_merge =  Algoritmo(BubbleSort())
        algoritmo_merge.ordenar(self.ventana)
        self.assertEqual(self.lista_ordenada, algoritmo_merge.lista_ordenada)

if __name__ == '__main__':
    unittest.main()