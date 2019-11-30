#############################
#                           #
#   Este é um cabeçalho     #
#   Luiz Henrique Rodrigues #
#                           #
#############################


import math


def focdasse(a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print ("raizes complexas")
    if delta == 0:
        raizUnica = - b/ (2 * a)
        
        print("raiz única :", raizUnica)
        return raizUnica
    if delta>0:
        Raiz = math.sqrt(delta)
        RaizUm = (-b+Raiz) / (2*a)
        print ("Raizes :", RaizUm, " e VV")
        RaizDois = (-b-Raiz) / (2*a)
        return RaizDois
        

    
print(focdasse(1,0,-1))

print(focdasse(1,2,-1))
print(focdasse(1,2,1))
print(focdasse(1,0,3))
