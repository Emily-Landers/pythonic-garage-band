import pytest

from garage_band.band import Band

def test_band_name():
    Devo = Band("Devo", [])
    assert  Devo.name == "Devo"
    
def test_band_str():
    Devo = Band("Devo", [])
    actual = str(Devo)
    expected = "The band Devo"
    assert actual == expected
    
def test_band_repr():
    Devo = Band("Devo", [])
    actual = repr(Devo)
    expected = "Band instance. name=Devo, members=[]"
    assert actual == expected

def test_band_list():
    #assert Band.to_list() == []
    Band("Devo", [])
    #assert len(Band.to_list()) == 1
    assert Band.to_list()[0] == "Devo"