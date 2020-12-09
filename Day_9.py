from Advent_of_Code import txt_to_array
import numpy as np
from numpy import random

def Day_9_Part_1(filepath,step_size):
    array = txt_to_array(filepath, "\n")
    step = step_size
    go = 1
    number = 0
    while go > 0:
        array_to_check = array[(step-step_size):step]
        sums = int(array[step])
        check = step
        for i in range(0,len(array_to_check)):
            for j in range(0,len(array_to_check)):
                val_1 = int(array_to_check[i])
                val_2 = int(array_to_check[j])
                if (val_1 != val_2) and ((val_1+val_2) == sums):
                    step = step +1
                    break
            if (val_1 != val_2) and ((val_1 + val_2) == sums):
                break

        if check == step:
            number = sums
            go = 0

    return number





def Day_9_Part_2(filepath,step_size):
    array = txt_to_array(filepath, "\n")
    step = step_size
    go = 1
    number = 0
    while go > 0:
        array_to_check = array[(step - step_size):step]
        sums = int(array[step])
        check = step
        for i in range(0, len(array_to_check)):
            for j in range(0, len(array_to_check)):
                val_1 = int(array_to_check[i])
                val_2 = int(array_to_check[j])
                if (val_1 != val_2) and ((val_1 + val_2) == sums):
                    step = step + 1
                    break
            if (val_1 != val_2) and ((val_1 + val_2) == sums):
                break

        if check == step:
            number = sums
            go = 0
    index_goal = step
    array_sliced = array[:index_goal]

    for i in range(0,len(array_sliced)):
        total = 0
        array_val = []
        for j in range(i,len(array_sliced)):
            total = total+int(array_sliced[j])
            array_val.append(int(array_sliced[j]))
            if total > number:
                break
            elif total == number:
                value = min(array_val)+max(array_val)

    return value



print("Day 9 Part 1 answer: ", Day_9_Part_1("Input\\Day_9.txt",25))
print("Day 9 Part 2 answer: ", Day_9_Part_2("Input\\Day_9.txt",25))
