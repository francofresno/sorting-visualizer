class QuickSort:
    comparaciones = 0
    def ordenar_numeros(self, lista_enteros):
        lista = lista_enteros
        self.quicksort(lista, 0, len(lista)-1)
        return lista

    def quicksort(self, lista, inicio, fin):
        if inicio < fin:
    	    pivote_indice = self.particionar(lista, inicio, fin)
    	    self.quicksort(lista, inicio, pivote_indice-1)
    	    self.quicksort(lista, pivote_indice+1, fin)

    def particionar(self, lista, inicio, fin):
	    pivote = lista[fin]
	    indice = inicio

	    for i in range(inicio, fin):
		    self.comparaciones += 1
		    if lista[i] <= pivote:
			    lista[indice], lista[i] = lista[i], lista[indice]
			    indice += 1

	    lista[indice], lista[fin] = lista[fin], lista[indice]
	    return indice

    def resetearComparaciones(self):
        self.comparaciones = 0