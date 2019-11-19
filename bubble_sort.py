class BubbleSort:
    comparaciones = 0
    def ordenar_numeros(self, lista_enteros):
        lista = lista_enteros
        tamanio = len(lista) - 1

        for i in range(1, tamanio):
            for j in range(tamanio - i):
                self.comparaciones += 1

                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
            
        return lista
    
    def resetearComparaciones(self):
        self.comparaciones = 0