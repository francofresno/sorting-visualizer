class ListaManager:
    lista_numeros = []

    def txt_a_lista(self, archivo):
        lista_previa = []
        lista_aplanada = []
        for linea in archivo.readlines():
            lista_previa.append(linea.rstrip().split(','))
        #aplanar la lista y quitar los ''
        lista_aplanada = [numero for sublista_previa in lista_previa for numero in sublista_previa if numero != '']
        self.convertirAListaDeInt(lista_aplanada)

    def convertirAListaDeInt(self, lista_aplanada):
        try:
           self.lista_numeros = list(map(int, lista_aplanada))
        except ValueError:
            print("Todos deben ser numeros")
        else:
            print(self.lista_numeros)