
import numpy as np
from pytest import raises
from binsearch import binary_search

input = list(range(10))


def test_binary_search():
    assert binary_search(input,5) == 5
    
def test_float():
    assert binary_search(input,4.5) == -1

def test_outside():
    assert binary_search(input, 10) == -1
    
def test_one_element():
    assert binary_search([5], 5) == 0
    
def test_inf():
    assert binary_search([1,2,np.inf], 2) == 1
    
def test_inf2():
    assert binary_search([1,2,np.inf], np.inf) == 2
    
def test_outside_left_right():
    assert binary_search(input, 5, 1,3) == -1

def test_wrong_left_right():
    assert binary_search(input, 2, 3, 1) == -1
    
def test_all_equals():
    assert binary_search(input, 2, 2, 2) == 2
            
def test_no_needle():
    with raises(TypeError):
        binary_search(input)

def test_char():
    with raises(TypeError):
        binary_search([input,'a'])