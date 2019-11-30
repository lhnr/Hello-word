import math


def focdasse(a,b,c):
    delta = b**2 - 4*a*c
if delta < 0:
    print ("raizes complexas")
if delta == 0:
    raizUnica = - b/ (2 * a)
    return: raizUnica
    print("raiz única :", raizUnica)
if delta>0:
    Raiz = math.sqrt(delta)
    RaizUm = (-b+Raiz) / (2*a)
    return RaizUm
    RaizDois = (-b-Raiz) / (2*a)
    return RaizDois
    print ("Raizes :", RaizUm," e ", RaizDois)

    
focdasse(1,2,-9)
focdasse(1,2,-1)
focdasse(1,2,1)
focdasse(1,2,0)

        










