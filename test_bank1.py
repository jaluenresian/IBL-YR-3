import pytest
from bank import value

def test_value():
    assert value("Hello world") == 0
    assert value("hi") == 20
    assert value("Goodbye") == 100
    assert value("") == 100
    assert value("H") == 20
    assert value("h") == 20
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hElLo") == 0