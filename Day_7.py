from Advent_of_Code import txt_to_array
import re

def Day_7_Part_1(filepath):
    rules = txt_to_array(filepath, "\n")
    array_shiny_gold_bags = []
    bag = 0
    array_bags = []
    num_bags = len(array_bags)
    while bag <= num_bags+1:
        print("bag", bag)
        if num_bags == 0:
            bag_name = "shiny gold"
        else:
            bag_name = array_bags[bag-1]
        for i in range(0, len(rules)):
            if (bag_name in rules[i]):
                array_shiny_gold_bags.append(rules[i].split(" bag",1)[0])

        for i in range(0,len(array_shiny_gold_bags)):
            if (array_shiny_gold_bags[i] not in array_bags) and (array_shiny_gold_bags[i] != "shiny gold"):
                array_bags.append(array_shiny_gold_bags[i])
        num_bags = len(array_bags)
        bag = bag +1
        if bag > num_bags:
            break

    return num_bags





def Day_7_Part_2(filepath):
    rules_original = txt_to_array(filepath, "\n")
    rules_split = []
    for i in range(0, len(rules_original)):
        x = re.split("contain|bags|bag|,",rules_original[i])
        rules_split.append(x)

    rules = []
    for i in range(0,len(rules_split)):
        rules_layer_1 = []
        for j in range(0,len(rules_split[i])):
            if (rules_split[i][j] == " ") or(rules_split[i][j] == ".") or (rules_split[i][j] == ""):
                None
            else:
                rules_layer_1.append(" ".join(rules_split[i][j].split()))
        rules.append(rules_layer_1)

    index_no_other = []
    for i in range(0,len(rules)):
        if rules[i][1] == "no other":
            index_no_other.append(i)

    dict_bags = {}
    for i in range(0,len(index_no_other)):
        bag = rules[index_no_other[i]][0]
        dict_bags[bag] = 1

    valid = 1
    while valid == 1:
        y = 0
        for i in range(0,len(rules)):
            x = 0
            for j in range(1,len(rules[i])):
                for bag_checked in dict_bags:
                    if bag_checked in rules[i][j]:
                        x = x+1
                if ((x == (len(rules[i]))-1)) and (rules[i][0] not in dict_bags):
                    dict_bags[rules[i][0]] = 0
                    for j in range(1, len(rules[i])):
                        dict_bags["Keep"] = dict_bags[rules[i][0]]
                        bag_val = rules[i][j].split(" ", 1)[1]
                        val = int(rules[i][j].split(" ", 1)[0])
                        dict_bags[rules[i][0]] = dict_bags["Keep"]+val * dict_bags[bag_val]
                        y = 1
                    if rules[i][0] != "shiny gold":
                        dict_bags["Keep"] = dict_bags[rules[i][0]]
                        dict_bags[rules[i][0]] = dict_bags["Keep"]+1
                    dict_bags["Keep"] = 0

        if y == 0:
            valid = 0
    return dict_bags["shiny gold"]


print("Day 7 Part 1 answer: ", Day_7_Part_1("Input\\Day_7.txt"))
print("Day 7 Part 2 answer: ", Day_7_Part_2("Input\\Day_7.txt"))
