def BinaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


bin_data = input("input binary data: ")

print("The binary value is:", bin_data)

str_data = " "

for i in range(0, len(bin_data), 7):
    temp_data = int(bin_data[i : i + 7])
    decimal_data = BinaryToDecimal(temp_data)
    str_data = str_data + chr(decimal_data)

print("The Binary value after string conversion is:", str_data)
