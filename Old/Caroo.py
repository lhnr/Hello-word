def main():
    carro1 = Carro('Brasília', 1986, 'amarela', 80)
    carro2 = Carro('Fuscão', 1989, 'preto', 95)

    carro1.acelere(1000)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)
    carro2.pare()


class Carro:
    def __init__(self, mod, ano, cor, VelMax):
        self.modelo = mod
        self.ano    = ano
        self.cor    = cor
        self.vel    = 0
        self.maxVel = VelMax    # Velocidade Máxima


    def imprima(self):
        if self.vel == 0:    # Só pardo podemos ver o ano do carro
            print( "%s %s %d"%(self.modelo, self.cor, self.ano))
        elif self.vel < self.maxVel:
            print( "%s %s indo a %d Km/h"%(self.modelo, self.cor, self.vel))
        else:
            print( "%s %s indo muito rápido!"%(self.modelo, self.cor))

    def acelere(self, velocidade):
        self.vel = velocidade
        if self.vel > self.maxVel:
            self.vel = self.maxVel
        self.imprima()

    def pare(self):
        self.vel = 0
        self.imprima()

main()
