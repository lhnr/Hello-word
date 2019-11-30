import pytest

def busca_bina(lista, elemento, min = 0, max = None):
    if max == None:
        max = len(lista) - 1

    if max < min:
        return False
    else:
        meio = min + (max - min) // 2

    if lista[meio] > elemento:
        return busca_bina(lista, elemento, min, meio - 1)

    elif lista[meio] < elemento:
        return busca_bina(lista, elemento, meio + 1, max)

    else: return meio

a = [1, 2, 3, 4, 5, 6]

@pytest.mark.parametrize("lista, valor, esperado",[
    (a, 1, 0),
    (a, 2, 1),
    (a, 3, 2),
    (a, 4, 3),
    (a, 5, 4),
    (a, 6, 5),
    (a, 7, False),
    (a, 15, False),
    (a, -1, False)
    ])

def testa_busca_bina(lista, valor, esperado):
    assert busca_bina(lista, valor) == esperado
