print("Hvað Viltu Gera")
user_input = input("And | Or | Xor | Not ")
user_input_lower = user_input.lower()


def add_tilda(binary):
    bits = [binary[i : i + 4] for i in range(0, len(binary), 4)]
    new_str = "-".join(bits)
    return new_str


if user_input_lower == "and":
    user_input_a = input("Binary 1: ")
    user_input_b = input("Binary 2: ")
    stadus_value = 0
    and_binary = ""
    while stadus_value != len(user_input_a):
        if user_input_a[stadus_value] == user_input_b[stadus_value]:
            and_binary += user_input_a[stadus_value]
            stadus_value += 1
        else:
            and_binary += "0"
            stadus_value += 1
    print(f"AND (&) {and_binary}")

elif user_input_lower == "or":
    user_input_a = input("Binary 1: ")
    user_input_b = input("Binary 2: ")
    stadus_value = 0
    or_binary = ""
    while stadus_value != len(user_input_a):
        if user_input_a[stadus_value] == "0" and user_input_b[stadus_value] == "0":
            or_binary += "0"
            stadus_value += 1
        elif user_input_a[stadus_value] == "1" or user_input_b[stadus_value] == "1":
            or_binary += "1"
            stadus_value += 1
        else:
            or_binary += "-"
            stadus_value += 1
    print(f"OR (|) {or_binary}")

elif user_input_lower == "xor":
    user_input_a = input("Binary 1: ")
    user_input_b = input("Binary 2: ")
    stadus_value = 0
    xor_binary = ""
    while stadus_value != len(user_input_a):
        if user_input_a[stadus_value] == "-":
            stadus_value += 1
            continue
        if user_input_a[stadus_value] == user_input_b[stadus_value]:
            xor_binary += "0"
            stadus_value += 1
        elif user_input_a[stadus_value] == "1" or user_input_b[stadus_value] == "1":
            xor_binary += "1"
            stadus_value += 1
        new_str = add_tilda(xor_binary)
    print(f"XOR (^) {new_str}")

elif user_input_lower == "not":
    user_input_a = input("Binary 1: ")
    not_binary = ""
    for i in user_input_a:
        if i == "0":
            not_binary += "1"
        elif i == "1":
            not_binary += "0"
    print(f"NOT (~) {not_binary}")
