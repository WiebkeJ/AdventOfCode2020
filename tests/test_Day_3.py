import pytest
from Day_3 import day_3_part_1,day_3_part_2

def test_day_3_part_1():
    file = "Input\\test_Day_3.txt"
    answer = day_3_part_1(file)
    assert (answer == 7)


def test_day_3_part_2():
    file = "Input\\test_Day_3.txt"
    answer = day_3_part_2(file)
    assert (answer == 336)