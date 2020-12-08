import pytest
from Day_7 import Day_7_Part_1, Day_7_Part_2

def test_day_7_part_1():
    assert(Day_7_Part_1("Input\\test_Day_7.txt") == 4)


@pytest.mark.parametrize("input, output",[("Input\\test_Day_7.txt",32), ("Input\\test_Day_7_2.txt",126)])
def test_day_7_part_2(input, output):
    assert (Day_7_Part_2(input) == output)