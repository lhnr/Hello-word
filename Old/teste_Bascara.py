import Bascara


class TestBarcara:
    

    def testa_uma_raiz(self):
        b = Bascara.Bascara()
        assert b.calcula(1,1,1) == 0
        
    def testa_uma_raiz(self):
        b = Bascara.Bascara()
        assert b.calcula(1,2,1) == (1,-1)

    def testa_uma_raiz(self):
        b = Bascara.Bascara()
        assert b.calcula(1,0,0) == (1,0)
        
    def testa_uma_raiz(self):
        b = Bascara.Bascara()
        assert b.calcula(1,-5,6) == (2,3,2)
