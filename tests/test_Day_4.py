import pytest
from Day_4 import day_4_part_1, day_4_part_2

def test_day_4_part_1():
    answer = day_4_part_1("Input\\test_Day_4.txt")
    assert(answer == 2)

def test_day_4_part_2():
    answer = day_4_part_2("Input\\test_Day_4_2.txt")
    assert(answer== 4)