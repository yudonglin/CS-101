import math

def decimalToBinary(num:int):
    binary_num_list = []
    while True:
        binary = num%2
        binary_num_list.append(int(binary))
        num = (num-binary)/2
        if num == 0:
            break
    binary_num_list.reverse()
    return binary_num_list

def binaryToDecimal(num:int):
    decimal_num_list = []
