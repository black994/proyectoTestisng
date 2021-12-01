import pytest
from pyson import campeones
from pyson import LeerURL


#run test default
def test_campeon():
    assert campeones == 102

def test_leerURL():
    assert LeerURL() == None


