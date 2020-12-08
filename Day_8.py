from Advent_of_Code import txt_to_array
import re
import copy

def Day_8_Part_1(filepath):
    array_original = txt_to_array(filepath, "\n")
    array = []
    for i in range(0,len(array_original)):
        x = re.split(" ", array_original[i])[0],int(re.split(" ", array_original[i])[1])
        array.append(x)
    num_acc = 0
    start = 0
    step = start
    while 1 > 0 :
        point = array[step]
        if len(point)<3:
            if point[0] == "nop":
                array[step] = (point[0],point[1],"Done")
                step = step + 1
            elif point[0] == "acc":
                num_acc = num_acc+point[1]
                array[step] = (point[0], point[1], "Done")
                step = step + 1
            elif point[0] == "jmp":
                array[step] = (point[0], point[1], "Done")
                step = step + point[1]
        else:
            break

    return num_acc

def Day_8_Part_2(filepath):
    array_original = txt_to_array(filepath, "\n")
    array = []
    for i in range(0,len(array_original)):
        x = re.split(" ", array_original[i])[0],int(re.split(" ", array_original[i])[1])
        array.append([x[0],x[1]])
    index_jmp = []
    index_nop = []
    print(array)
    print(array[0])
    for i in range(0,len(array)):
        if array[i][0] == "jmp":
            index_jmp.append(i)
        elif array[i][0] == "nop":
            index_nop.append(i)
    step = 0
    finished = 0
    while step < len(array):
        for i in range(0, len(index_jmp)):
            array_copy = copy.deepcopy(array)
            array_copy[index_jmp[i]][0] = "nop"
            num_acc = 0
            start = 0
            step = start
            con = 1
            while con > 0:
                point = array_copy[step]
                if len(point) < 3:
                    if point[0] == "nop":
                        array_copy[step] = (point[0], point[1], "Done")
                        step = step + 1
                    elif point[0] == "acc":
                        num_acc = num_acc + point[1]
                        array_copy[step] = (point[0], point[1], "Done")
                        step = step + 1
                    elif point[0] == "jmp":
                        array_copy[step] = (point[0], point[1], "Done")
                        step = step + point[1]
                    if step == len(array_copy):
                        con = 0
                        finished = 1
                        i = len(array)
                else:
                    con = 0
                    break
            if finished == 1:
                break
        if finished == 0:
            for i in range(0, len(index_nop)):
                array_copy = copy.deepcopy(array)
                array_copy[index_jmp[i]][0] = "jmp"
                num_acc = 0
                start = 0
                step = start
                con = 1
                while con > 0:
                    point = array_copy[step]
                    if len(point) < 3:
                        if point[0] == "nop":
                            array_copy[step] = (point[0], point[1], "Done")
                            step = step + 1
                        elif point[0] == "acc":
                            num_acc = num_acc + point[1]
                            array_copy[step] = (point[0], point[1], "Done")
                            step = step + 1
                        elif point[0] == "jmp":
                            array_copy[step] = (point[0], point[1], "Done")
                            step = step + point[1]
                        if step == len(array_copy):
                            finished = 1
                            i = len(array)
                    else:
                        con = 0
                if finished == 1:
                    i = len(array)
    return num_acc

#print("Day 8 Part 1 answer: ",Day_8_Part_1("Input\\Day_8.txt"))
print("Day 8 Part 2 answer: ",Day_8_Part_2("Input\\Day_8.txt"))