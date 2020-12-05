import numpy as np
from numpy import random

from Advent_of_Code import txt_to_array, num_txt_to_array, prod

# Day 1 Part 1
def day_1_part_1(filepath):
    array = num_txt_to_array(filepath)
    array_sorted = np.sort(array)
    find_values = True
    while find_values == True:
        sum_2020 = array_sorted[0]+array_sorted[-1]
        if sum_2020 < 2020:
            array_sorted = array_sorted[1:]
        elif sum_2020 > 2020:
            array_sorted = array_sorted[:-1]
        elif sum_2020 == 2020:
            find_values == False
            break
    answer = prod(array_sorted[0], array_sorted[-1])
    return answer

print("Day 1 Part 1 answer: ", day_1_part_1("Input\\test_Day_1.txt"))


# Day 1 Part 2

def day_1_part_2(filepath):
    array = num_txt_to_array(filepath)
    find_values = True
    while find_values == True:
        val_1 = random.choice(array)
        val_2 = random.choice(array)
        val_3 = random.choice(array)
        sum_2020 = val_1+val_2+val_3
        if sum_2020 == 2020:
            product = val_3*val_2*val_1
            find_values = False
            break
    return product

print("Day 1 Part 2 answer: ", day_1_part_2("Input\\test_Day_1.txt"))