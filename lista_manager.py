class ListaManager:
    lista_numeros = []
    flag_lista_invalida = False

    def txt_a_lista(self, archivo):
        lista_previa = []
        lista_aplanada = []
        for linea in archivo.readlines():
            lista_previa.append(linea.rstrip().split(','))
        lista_aplanada = self.aplanar_lista(lista_previa)
        self.convertir_a_lista_de_ints(lista_aplanada)

    def aplanar_lista(self, lista_a_aplanar):
        #aplanar la lista y quitar los ''
        return [numero for sublista_previa in lista_a_aplanar for numero in sublista_previa if numero != '']

    def convertir_a_lista_de_ints(self, lista_aplanada):
        try:
            self.lista_numeros = list(map(int, lista_aplanada))
            self.flag_lista_invalida = False
        except ValueError:
            self.flag_lista_invalida = True
            raise ValueError("Lista invalida")