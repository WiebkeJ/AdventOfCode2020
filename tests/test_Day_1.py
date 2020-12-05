import pytest
from Day_1 import day_1_part_1, day_1_part_2

def test_day_1_part_1():
    file = "Input\\test_Day_1.txt"
    answer = day_1_part_1(file)
    assert (answer == 514579)

def test_day_1_part_2():
    file = "Input\\test_Day_1.txt"
    answer  =  day_1_part_2(file)
    assert (answer == 241861950)