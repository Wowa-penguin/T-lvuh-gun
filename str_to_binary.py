user_input_str = input("Enter binary: ")

print("The original string is : " + str(user_input_str))

res = "".join(format(ord(i), "08b") for i in user_input_str)

print("The string after binary conversion : " + str(res))
