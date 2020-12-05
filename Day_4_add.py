from Advent_of_Code import get_string


def birth_year_4_2(string):
    valid = 0
    info = get_string(string, ":", "a")
    #print("info", info, string)
    if (info.isdigit() == True):
        #print("CHeck")
        if (int(info)>= 1920) and (int(info) <=2002):
            valid = 1
    return valid

def issue_year_4_2(string):
    valid = 0
    info = get_string(string, ":", "a")
    if (info.isdigit() == True):
        if (int(info)>= 2010) and (int(info) <=2020):
            valid = 1
    return valid

def expiration_year_4_2(string):
    valid = 0
    info = get_string(string, ":", "a")
    if (info.isdigit() == True):
        if (int(info)>= 2020) and (int(info) <=2030):
            valid = 1

    return valid

def height_4_2(string):
    valid = 0
    info = get_string(string, ":", "a")
    if "cm" in info:
        value = int(get_string(info,"c","b"))
        if (value >=150) and (value <=193):
            valid = 1
    elif "in" in info:
        value = int(get_string(info, "i", "b"))
        if (value >=59) and (value <=76):
            valid = 1
    return valid


def hair_4_2(string):
    valid = 0
    info = get_string(string, ":", "a")
    if (info[0] == "#") and (len(info)==7):
        char = ("#,0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f")
        result = info
        for character in char:
            result = result.replace(character,"")
        if len(result)==0:
            valid = 1
    return valid


def eyes_4_2(string):
    valid = 0
    info = get_string(string, ":", "a")
    colours = ["amb","blu","brn","gry","grn","hzl","oth"]
    if info in colours:
        valid = 1
    return valid


def passport_4_2(string):
    valid = 0
    info = get_string(string, ":", "a")
    if (info.isdigit()==True) and (len(info)==9):
        valid = 1
    return valid



def check_validation_4_2(string):
    for i in range(0,len(string)):
        valid = 0
        if "byr" in string[i]:
            valid = birth_year_4_2(string[i])
        elif "iyr" in string[i]:
            valid = issue_year_4_2(string[i])
        elif "eyr" in string[i]:
            valid = expiration_year_4_2(string[i])
        elif "hgt" in string[i]:
            valid = height_4_2(string[i])
        elif "hcl" in string[i]:
            valid = hair_4_2(string[i])
        elif "ecl" in string[i]:
            valid = eyes_4_2(string[i])
        elif "pid" in string[i]:
            valid = passport_4_2(string[i])
        elif "cid" in string[i]:
            valid = 1
        if valid == 0:
            break
    return valid

