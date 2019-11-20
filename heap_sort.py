class HeapSort:
    comparaciones = 0
    nombre = "Heap Sort"

    def ordenar_numeros(self, lista_enteros):
        lista = lista_enteros
        tamanio = len(lista)

        for i in range(tamanio, -1, -1):
            self.heapify(lista, tamanio, i)
    
        for i in range(tamanio-1, -1, -1):
            lista[i], lista[0] = lista[0], lista[i]  
            self.heapify(lista, i, 0)

        return lista

    def heapify(self, lista, tamanio, i):
        mas_grande = i
        izquierda = 2 * i + 1
        derecha = 2 * i + 2
        self.comparaciones += 1



        if izquierda < tamanio and lista[i] < lista[izquierda]:
            mas_grande = izquierda
 
        if derecha < tamanio and lista[mas_grande] < lista[derecha]:
            mas_grande = derecha

        if mas_grande != i:
            lista[i],lista[mas_grande] = lista[mas_grande],lista[i]
            self.heapify(lista, tamanio, mas_grande)

    def resetearComparaciones(self):
        self.comparaciones = 0