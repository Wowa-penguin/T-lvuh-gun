print("Enter a binary with this sign (-) to shift it")
user_input_binary = input("Binary: ")
print("Shift << == left or right == >>")
user_input_shift = input("(left) or (right)) ")
print("how many steps")
user_input_steps = int(input("Steps: "))
print(f"{user_input_binary} (old binery)")
binary = user_input_binary.replace("-", "")

add_0 = user_input_steps * "0"
# <<
if user_input_shift[0] == "l":
    shiftit_binery = binary[user_input_steps:] + add_0
    bits = [shiftit_binery[i : i + 4] for i in range(0, len(shiftit_binery), 4)]
    new_str = "-".join(bits)
    print(new_str)
elif user_input_shift[0] == "r":
    shiftit_binery = add_0 + binary[:-user_input_steps]
    bits = [shiftit_binery[i : i + 4] for i in range(0, len(shiftit_binery), 4)]
    new_str = "-".join(bits)
    print(new_str)
