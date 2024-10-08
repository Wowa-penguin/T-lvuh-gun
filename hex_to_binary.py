def add_tilda(binary):
    bits = [binary[i : i + 4] for i in range(0, len(binary), 4)]
    new_str = "-".join(bits)
    return new_str


print("Enter a hexadesimal: ")
user_input_hex = input("Ender hex: ")
digits = len(user_input_hex) * 4

int_for_hex = int(user_input_hex, 16)
binary = bin(int_for_hex)
binary = binary[2:]

while len(binary) != digits:
    binary = "0" + binary

new_str = add_tilda(binary)

print(new_str)
