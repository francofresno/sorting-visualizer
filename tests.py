import unittest
from ventana import *
from sorting_algorithms import *
from merge_sort import *
from heap_sort import *
from bubble_sort import *
from quick_sort import *

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