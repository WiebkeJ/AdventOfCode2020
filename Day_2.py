from Advent_of_Code import txt_to_array

def check_string_2_1(string):
    index_1 = string.find("-")
    index_2 = string.find(" ")
    index_3 = string.find(":")

    val_1 = int(string[:index_1])
    val_2 = int(string[index_1+1:index_2])
    char = string[index_3-1]
    password = string[index_3+1:]
    number_of_char = password.count(char)
    if (number_of_char>= val_1) and (number_of_char<= val_2):
        valid = True
    else:
        valid = False
    return valid


def check_string_2_2(string):
    index_1 = string.find("-")
    index_2 = string.find(" ")
    index_3 = string.find(":")

    val_1 = int(string[:index_1])
    val_2 = int(string[index_1 + 1:index_2])
    char = string[index_3 - 1]
    password = string[index_3 + 1:]

    if (password[val_1] == char) and (password[val_2] != char):
        valid = True
    elif (password[val_1] != char) and (password[val_2] == char):
        valid = True
    else:
        valid = False
    return valid

def day_2_part_1(filepath):
    list_of_passwords = txt_to_array(filepath, "\n")
    num_of_valid_passwords = 0
    for i in range(0, len(list_of_passwords)):
        valid = check_string_2_1(list_of_passwords[i])
        if valid == True:
            num_of_valid_passwords = num_of_valid_passwords+1

    return num_of_valid_passwords

def day_2_part_2(filepath):
    list_of_passwords = txt_to_array(filepath, "\n")
    num_of_valid_passwords = 0
    for i in range(0, len(list_of_passwords)):
        valid = check_string_2_2(list_of_passwords[i])
        if valid == True:
            num_of_valid_passwords = num_of_valid_passwords + 1

    return num_of_valid_passwords


print("Day 2 Part 1 answer: ", day_2_part_1("Input\\Day_2.txt"))
print("Day 2 Part 2 answer: ", day_2_part_2("Input\\Day_2.txt"))