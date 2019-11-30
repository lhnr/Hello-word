import ordenador
import time
import random
import buscador


class Buscador:
    def busca_sequencial(self, lista, x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
            return -1
        
    def busca_binaria(self, n, x):
        lista = self.lista_aleatoria(n)
        lista[n//10] = 55
        o = ordenador.Ordenador()
        o.bolha_curta(lista)
        # print(lista)
        primeiro = 0
        ultimo = len(lista) - 1
        antes_total = time.time()
        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2
            if lista[meio] == x:
                depois_total = time.time()
                print ("\n Tempo de busca encontrando =", depois_total - antes_total)
                return meio            
            else:
                if x < lista[meio]:
                        ultimo = meio - 1
                else:
                        primeiro = meio + 1
        depois_total = time.time()
        print ("\n Tempo de busca sem encontrar =", depois_total - antes_total)
        return -1
    


    def lista_aleatoria(self, n):
        antes = time.time()
        lista = [random.randrange(1000) for x in range(n)]
        depois = time.time()
        print ("Tempo de geracao randomica =", depois - antes)
        return lista

    
    def tempo_ordena_busca(n):
        
        o = ordenador.Ordenador()
        lista = self.lista_aleatoria(n)
        antes = time.time()
        o.bolha_curta(lista)
        depois = time.time()
        print ("\n Tempo de ordenacao =", depois - antes)

    
