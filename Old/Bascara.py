import math


class Bascara:

    def delta (self, a,b,c):
        return b ** 2 - 4 * a * c

    def main(self):
        a_dig = float(input("Digite a :"))
        b_dig = float(input("Digite b :"))
        c_dig = float(input("Digite c :"))
        print(self.calcula(a_dig,b_dig,c_dig))
        
    def calcula (self, a, b, c):
        d = self.delta( a, b, c)

        if d == 0:
            raizUnica = (- b + math.sqrt(d))/ (2 * a)
            return 1, raizUnica
        else:
                if d < 0:
                    return 0
                else:
                        Raiz = math.sqrt(d)
                        RaizUm = (-b+Raiz) / (2*a)
                        RaizDois = (-b-Raiz) / (2*a)
                        return 2, RaizUm, RaizDois
