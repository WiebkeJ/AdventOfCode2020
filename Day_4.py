from Advent_of_Code import txt_to_array
from Day_4_add import check_validation_4_2
import re

# addtional functions for Day 4 Part 2



#######################################################
def day_4_part_1(filepath):
    array_original = txt_to_array(filepath, "\n\n")
    array_to_sort = []
    for i in range(0 ,len(array_original)):
        array_to_add = re.split('\n| ', array_original[i])
        array_to_sort.append(array_to_add)
    array = sorted(array_to_sort,key = len)
    valid = 0
    for i in range(len(array),0,-1):
        if len(array[i-1]) < 7:
            break
        elif len(array[i-1]) == 7:
            add_valid = 1
            for j in range(0, len(array[i-1])):
                if "cid" in array[i-1][j]:
                    add_valid = 0
            valid = valid + add_valid
        elif len(array[i-1]) == 8:
            valid = valid +1
    return valid

def day_4_part_2(filepath):
    array_original = txt_to_array(filepath, "\n\n")
    array_to_sort = []
    for i in range(0 ,len(array_original)):
        array_to_add = re.split('\n| ', array_original[i])
        array_to_sort.append(array_to_add)
    array = sorted(array_to_sort,key = len)
    valid = 0
    for i in range(0,len(array)):
        if len(array[i]) < 7:
            add_valid = 0
        elif len(array[i]) >= 7:
            add_valid = 1
            check_val = 1
            for j in range(0, len(array[i])):
                if ("cid" in array[i][j]) and (len(array[i])==7):
                    add_valid = 0
                    check_val = 0
            if check_val == 1:
                    add_valid = check_validation_4_2(array[i])
        valid = valid + add_valid

    return valid

print("Day 4 Part 1 answer: ",day_4_part_1("Input\\Day_4.txt"))
print("Day 4 Part 2 answer: ",day_4_part_2("Input\\Day_4.txt"))
