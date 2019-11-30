numNum = int(input("Quantos números você quer somar? :"))
soma = 0
while numNum > 0:
    numNovo = int(input("Digite um número para somar :"))
    soma = soma + numNovo
    numNum = numNum - 1
print ("A soma é :", soma)
                  
