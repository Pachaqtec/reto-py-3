""" Tests for maths.py """
import pytest

from ordenar import ordenarArray

def test_ordenarArray():
    """ Test sumando 2 numeros """
    numeros = [1, 3, 5, 7, 9]
    assert 9 == ordenarArray(numeros)


