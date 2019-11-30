def cria_matriz(num_linhas, num_colunas):
    ''' (int, int) -> Matriz (listas de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas
    colunas em que cada elemento é digitado pelo usuário
    '''

    matriz = [] # lista vazia
    for i in range(num_linhas):
        # cria a linha i
        linha = [] # lista vazia
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) +"][" + str(j) + "]"))
            linha.append(linha)

        # adiciona linha i à matriz
        matriz.append(linha)

    return matriz

def ler_matriz():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    cria_matriz(lin,col)

