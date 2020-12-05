import pytest
from Day_5 import day_5_part_1, day_5_part_2, seat_ID

@pytest.mark.parametrize("seat,value",[("FBFBBFFRLR",357),("BFFFBBFRRR", 567),("FFFBBBFRRR",119),("BBFFBBFRLL",820)])
def test_seat_ID(seat,value):
    assert (seat_ID(seat)==value)

def test_day_5_part_1():
    assert (day_5_part_1("Input\\test_Day_5.txt")==820)
