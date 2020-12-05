import pytest
from Day_2 import day_2_part_1, day_2_part_2

def test_day_2_part_1():
    file = "Input\\test_Day_2.txt"
    answer = day_2_part_1(file)
    assert (answer == 2)


def test_day_2_part_2():
    file = "Input\\test_Day_2.txt"
    answer = day_2_part_2(file)
    assert (answer == 1)