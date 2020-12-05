from Advent_of_Code import txt_to_array

def day_3_part_1(filepath):
    array = txt_to_array(filepath, "\n")
    expanded_array = []
    for i in range(0,len(array)):
        expanded_array.append(array[i]*100)
    a=0
    b = 0
    tree = 0
    for i in range(0, len(expanded_array)-1):
        a = a+1
        b = b+3
        if expanded_array[a][b] == "#":
            tree = tree+1
    return tree

def day_3_part_2(filepath):
    array = txt_to_array(filepath, "\n")
    expanded_array = []
    for i in range(0,len(array)):
        expanded_array.append(array[i]*len(array))
    trees = []
    list_to_check = [[1,1],[1,3],[1,5],[1,7],[2,1]]
    for i in range(0, len(list_to_check)):
        a = 0
        b = 0
        tree = 0
        for j in range(0, len(expanded_array)-list_to_check[i][0],list_to_check[i][0]):
            a = a + list_to_check[i][0]
            b = b+list_to_check[i][1]
            if expanded_array[a][b] == "#":
                tree = tree +1
        trees.append(tree)
    product = 1
    for k in range(0,len(trees)):
        product = product*trees[k]
    return product


print("Day 3 Part 1 answer: ", day_3_part_1("Input\\Day_3.txt"))
print("Day 3 Part 2 answer: ", day_3_part_2("Input\\Day_3.txt"))