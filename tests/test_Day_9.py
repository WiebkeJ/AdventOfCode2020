import pytest
from Day_9 import Day_9_Part_1, Day_9_Part_2

def test_day_9_part_1():
    assert (Day_9_Part_1("Input\\test_Day_9.txt",5) == 127)


def test_day_9_part_2():
    assert(Day_9_Part_2("Input\\test_Day_9.txt",5) == 62)