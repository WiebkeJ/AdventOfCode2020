import numpy as np

def txt_to_array(filepath, splt):
    text_file=open(filepath, "r")
    array = text_file.read().split(splt)
    text_file.close()
    return array

def num_txt_to_array(filepath):
    array = np.genfromtxt(filepath)
    return array

def prod(a,b):
    product = a*b
    return product


def get_string(string, char, b_or_a):
    index = string.find(char)
    if b_or_a == "a":
        part_string = string[index+1:]
    elif b_or_a == "b":
        part_string = string[:index]
    return part_string