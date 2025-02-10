import math


def binary_list(num):
    arr = []
    int_part = int(num)
    fractional_part = num - int_part


    fractional_binary = []
    while fractional_part:
        fractional_part *= 2
        bit = int(fractional_part)
        fractional_binary.append(bit)
        fractional_part -= bit
        if len(fractional_binary) > 56:  # Limit the length to avoid infinite loop
            break
    if int_part != 0:
        int_part = bin(int_part).replace("0b", "")
        for i in (int_part):
            arr.append(int(i))

    full_num = arr + fractional_binary  # Correctly concatenate the integer and fractional parts
    exponent = -len(arr)

    while full_num[0] == 0:
        full_num.pop(0)
        exponent += 1
        
    return full_num, exponent

num = 2.3

full_num, exponent = binary_list(num)

print(full_num)
print(exponent)


x_minus = full_num[:53]

x_minus_int = int(''.join(str(bit) for bit in x_minus), 2)

x_plus, x_plus_ex = binary_list(x_minus_int)

print(x_plus)

