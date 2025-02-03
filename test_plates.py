import pytest

from plates import is_valid

def test_is_valid0():
    assert is_valid('CS50') == True
    assert is_valid("HELLO") == True

def test_is_valid1():
    assert is_valid('CS50P') == False


def test_is_valid2():
    assert is_valid('PI3.14') == False

def test_is_valid3():
    assert is_valid('OUTATIME') == False
    
def test_is_valid4():    
    assert is_valid('50CS') == False

def test_zero_placement():    
    assert is_valid("AB012") == False  # Starts with 0 in numbers
    assert is_valid("AB12") == True    # Valid
    assert is_valid("AB01CD") == False  # Numbers must not be followed by letters

def test_alpha():
    assert is_valid("123ABC") == False  # Does not start with letters
    assert is_valid("A1BC") == False    # Only one starting letter
    assert is_valid("AB12") == True    # Correct format
    assert is_valid("1A12") == False    # 



def test_starts_with_two_letters():
    assert is_valid("CS50") == True
    assert is_valid("C5") == False
    assert is_valid("5CS") == False

def test_length():
    assert is_valid("CS50") == True
    assert is_valid("C") == False
    assert is_valid("OUTATIME") == False

def test_numbers_at_end():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False

def test_no_punctuation():
    assert is_valid("PI314") == True
    assert is_valid("PI3.14") == False
    assert is_valid("PI 314") == False
