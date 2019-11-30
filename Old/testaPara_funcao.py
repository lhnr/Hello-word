def soma(x,y):
    return x+y

import pytest

@pytest.mark.parametrize("ent_x, ent_y, esperado", [
    (1,1,2),
    (3,1,4),
    (25,-1,24)
    ])

def testa_soma(ent_x, ent_y, esperado):
    assert soma(ent_x, ent_y) == esperado
