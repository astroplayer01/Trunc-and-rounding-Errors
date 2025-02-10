def float_to_binary(num):
    if num == 0:
        return "0.0 x 2^0"

    # Separate the number into its integer and fractional parts
    integer_part = int(num)
    fractional_part = num - integer_part

    # Convert the integer part to binary
    integer_binary = bin(integer_part).replace("0b", "")

    # Convert the fractional part to binary
    fractional_binary = []
    while fractional_part:
        fractional_part *= 2
        bit = int(fractional_part)
        fractional_binary.append(str(bit))
        fractional_part -= bit
        if len(fractional_binary) > 70:  # Limit the length to avoid infinite loop
            break

    # Combine the integer and fractional parts
    binary_representation = f"{integer_binary}.{''.join(fractional_binary)}"

    # Normalize the binary representation
    if integer_part != 0:
        exponent = len(integer_binary) - 1
        normalized_binary = f"0.{integer_binary[1:]}{''.join(fractional_binary)}"
    else:
        first_one_index = fractional_binary.index('1')
        exponent = -(first_one_index + 1)
        normalized_binary = f"0.{''.join(fractional_binary[first_one_index + 1:])}"

    # Ensure the mantissa is 64 bits
    mantissa = normalized_binary.split('.')[1]
    if len(mantissa) < 64:
        mantissa = mantissa.ljust(64, '0')
    else:
        mantissa = mantissa[:64]

    return mantissa, (exponent + 1)

# Example usage
machine_eps = 2**-53
num = 8.2
print(float_to_binary(num))