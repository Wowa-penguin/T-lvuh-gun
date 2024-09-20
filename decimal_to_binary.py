def add_tilda(binary):
    bits = [binary[i : i + 4] for i in range(0, len(binary), 4)]
    new_str = "-".join(bits)
    return new_str


print("Enter an decimal to convert to binary")
user_input_decimal = int(input("Input decimal: "))
print("(0 for null)")
user_input_digits = int(input("How many digits: "))
count = 0
binary = ""

while user_input_decimal > 0:
    if user_input_decimal % 2 == 1:
        binary += "1"
        count += 1
        user_input_decimal = user_input_decimal // 2
    elif user_input_decimal % 2 == 0:
        binary += "0"
        count += 1
        user_input_decimal = user_input_decimal // 2

if user_input_digits == 0:
    user_input_digits = len(binary)

while len(binary) != user_input_digits:
    binary = binary + "0"

new_str = add_tilda(binary)

print(new_str[::-1])
print(f"Digits = {len(binary)}")
