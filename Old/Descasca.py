numDESCASCA = int(input("Digite um número :"))
soma = 0
while numDESCASCA > 0:
    soma = soma + (numDESCASCA%10)
    numDESCASCA = numDESCASCA//10

print ("Soma do número descascado é :", soma)
