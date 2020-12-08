import pytest
from Day_6 import Day_6_Part_1, Day_6_Part_2

def test_Day_6_Part_1():
    assert(Day_6_Part_1("Input\\test_Day_6.txt")==11)

def test_Day_6_Part_2():
    assert(Day_6_Part_2("Input\\test_Day_6.txt")==6)