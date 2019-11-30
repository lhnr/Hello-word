import Bascara
import pytest

class TestBarcara:

    bac = Bascara.Bascara()
    
    @pytest.mark.parametrize("ae, be, ce, num_raizes",[
        (1,1,1,0)
        ])

    def testa_Para(ae, be, ce, num_raizes):
        assert bac.calcula(ae, be, ce) == num_raizes




#   def b(self):
#        return Bascara.Bascara()
    

