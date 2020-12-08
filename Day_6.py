from Advent_of_Code import txt_to_array
import re

def Day_6_Part_1(filepath):
    array_original = txt_to_array(filepath,"\n\n")
    array = []
    for i in range(0 ,len(array_original)):
        array_to_add = re.split('\n| ', array_original[i])
        array.append(array_to_add)

    char=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    counter = 0
    for i in range(0,len(array)):
        for character in char:
            found = 0
            for j in range(0,len(array[i])):
                if array[i][j].find(character) >= 0:
                    found = 1
            if found == 1:
                counter = counter+1
    return counter

def Day_6_Part_2(filepath):
    array_original = txt_to_array(filepath, "\n\n")
    array = []
    for i in range(0, len(array_original)):
        array_to_add = re.split('\n| ', array_original[i])
        array.append(array_to_add)

    char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]
    counter = 0
    for i in range(0, len(array)):
        for character in char:
            found = 0
            for j in range(0, len(array[i])):
                if array[i][j].find(character) >= 0:
                    found = found + 1
            if found == len(array[i]):
                counter = counter + 1
    return counter


print("Day 6 Part 1 answer: ", Day_6_Part_1("Input\\Day_6.txt"))
print("Day 6 Part 2 answer: ", Day_6_Part_2("Input\\Day_6.txt"))