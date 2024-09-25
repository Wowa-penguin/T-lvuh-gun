user_input_bin_1 = input("Enter the first binary: ")
user_input_bin_2 = input("Enter the second binary: ")
counter = len(user_input_bin_1)
bin_1_revers = user_input_bin_1[::-1]
bin_2_revers = user_input_bin_2[::-1]


def add_tilda(binary):
    bits = [binary[i : i + 4] for i in range(0, len(binary), 4)]
    new_str = "-".join(bits)
    return new_str


binary_result = ""
carry = False

for i in range(counter):
    first_bin = bin_1_revers[i]
    second_bin = bin_2_revers[i]
    if first_bin == "-":
        continue

    if (
        carry
        and first_bin == "1"
        and second_bin == "0"
        or first_bin == "0"
        and second_bin == "1"
    ):
        binary_result += "0"
        continue
    elif carry and first_bin == "0" and second_bin == "0":
        binary_result += "1"
        carry = False
        continue
    elif carry and first_bin == "1" and second_bin == "1":
        binary_result += "1"
        continue
    elif carry and first_bin == "0" and second_bin == "0":
        binary_result += "1"
        carry = False
        continue

    if first_bin == "1" and second_bin == "1":
        binary_result += "0"
        carry = True
    elif first_bin == "0" and second_bin == "0":
        binary_result += "0"
    elif (
        first_bin == "0" and second_bin == "1" or first_bin == "1" and second_bin == "0"
    ):
        binary_result += "1"
result = add_tilda(binary_result)
if carry:
    print("It Overflows")
    print(f"1-{result[::-1]}")
else:
    print(f"  {user_input_bin_1}")
    print(f"+ {user_input_bin_2}")
    print(f"  {counter * "-"}")
    print(f"  {result[::-1]}")
