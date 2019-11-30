class Ordenador:
    def selecao_direta(self, lista_entrada):

        fim = len(lista_entrada)

        for i in range(fim - 1):

            posicao_do_minimo = i

            for j in range(i+1, fim):
                if lista_entrada[j] < lista_entrada[posicao_do_minimo]:
                    posicao_do_minimo = j


            lista_entrada[i], lista_entrada[posicao_do_minimo] = lista_entrada[posicao_do_minimo],  lista_entrada[i]

    def bolha(self, lista):
        fim = len (lista)

        for i in range(fim-1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    trocou = True
            if not trocou:
                return

    def bolha_curta(self, lista):
        fim = len (lista)

        for i in range(fim-1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    trocou = True
            if not trocou:
                return
