class MergeSort:
    comparaciones = 0
    def ordenar_numeros(self, lista_enteros):
        if len(lista_enteros) <= 1:
            return lista_enteros

        mitad = len(lista_enteros) // 2
        parte_izquierda = lista_enteros[:mitad]
        parte_derecha = lista_enteros[mitad:]

        parte_izquierda = self.ordenar_numeros(parte_izquierda)
        parte_derecha = self.ordenar_numeros(parte_derecha)

        return self.merge(parte_izquierda, parte_derecha)

    def merge(self, parte_izquierda, parte_derecha):
        lista_nueva_ordenada = []
        i = 0
        j = 0

        # Intercalamos ordenadamente las dos listas
        while i < len(parte_izquierda) and j < len(parte_derecha):
            self.comparaciones += 1
            if parte_izquierda[i] < parte_derecha[j]:
                lista_nueva_ordenada.append(parte_izquierda[i])
                i += 1
            else:
                lista_nueva_ordenada.append(parte_derecha[j])
                j += 1
                
        # Agregamos las dos partes al resultado
        while i < len(parte_izquierda):
            lista_nueva_ordenada.append(parte_izquierda[i])
            i += 1
        while j < len(parte_derecha):
            lista_nueva_ordenada.append(parte_derecha[j])
            j += 1

        return lista_nueva_ordenada

    def resetearComparaciones(self):
        self.comparaciones = 0