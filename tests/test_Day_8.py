import pytest
from Day_8 import Day_8_Part_1, Day_8_Part_2

def test_day_8_part_1():
    assert(Day_8_Part_1("Input\\test_Day_8.txt") == 5)

def test_day_8_part_2():
    assert(Day_8_Part_2("Input\\test_Day_8.txt") == 8)