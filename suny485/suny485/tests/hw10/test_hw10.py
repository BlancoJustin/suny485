import pytest
from suny485.projects.hw10.fruit_query import is_it_a_fruit 

def test_is_it_a_fruit_bannana():
    assert is_it_a_fruit('bananna') is True

def test_is_it_a_fruit_orange():
    assert is_it_a_fruit('orange') is False

list1 = ['apple','pear']
def test_is_it_a_fruit_list():
    assert is_it_a_fruit(list1) is False

def test_is_it_a_fruit_int():
    assert is_it_a_fruit(3) is False

def test_is_it_a_fruit_float():
    assert is_it_a_fruit(3.7) is False


