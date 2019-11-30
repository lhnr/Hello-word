import time
import random
import ordenador




class Conta_Tempos:
    
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista

    def lista_quase(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara (self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]
        lista3 = lista1[:]

        o = ordenador.Ordenador()

        print("Comparacao com listas aleatorias")

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("Bolha demorou ", depois - antes, "segundos")


        antes = time.time()
        o.bolha_curta(lista3)
        depois = time.time()
        print("Bolha curta demorou ", depois - antes, "segundos")
        
    
        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Selecao Direta demorou ", depois - antes, "segundos")

        print("Comparacao com listas quase ordenadas")

        lista1 = self.lista_quase(n)
        lista2 = lista1[:]
        lista3 = lista1[:]

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("Bolha demorou ", depois - antes, "segundos")

        
        antes = time.time()
        o.bolha_curta(lista3)
        depois = time.time()
        print("Bolha curta demorou ", depois - antes, "segundos")
        
    
        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Selecao Direta demorou ", depois - antes, "segundos")



