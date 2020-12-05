from Advent_of_Code import txt_to_array

def seat_ID(string):
    rows = []
    columns = []
    for i in range(0,127+1):
        rows.append(i)
    for i in range(0,7+1):
        columns.append((i))
    #print("Start: ", rows, columns)
    for i in range(0,len(string)):
        if string[i] == "B":
            x = int(len(rows)/2)
            #print("x:", x)
            rows = rows[x:]
            #print("SchrittB", rows)
        elif string[i] == "F":
            x = int(len(rows)/2)
            rows = rows[:x]
            #print("SchrittF", rows)
        elif string[i] == "R":
            x = int(len(columns)/2)
            columns = columns[x:]
            #print("SchrittR", columns)
        elif string[i] == "L":
            x = int(len(columns)/2)
            columns = columns[:x]
            #print("SchrittL", columns)
    seat_ID = rows[0]*8+columns[0]
    return seat_ID



def day_5_part_1(filepath):
    array = txt_to_array(filepath,"\n")
    result = [0]
    for i in range(0, len(array)):
        val = seat_ID(array[i])
        if val > result[0]:
            result[0]=val
    return result[0]



def day_5_part_2(filepath):
    return

print("Day 5 Part 1 answer: ", day_5_part_1("Input\\Day_5.txt"))