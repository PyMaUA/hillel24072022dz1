username = input("Please tell me your name ")

str_for_slice = " maSHa "
print("slice between 1 and 6 --> ", str_for_slice[1:6])
new_string = f"{str_for_slice[1:6]}"
print(new_string)

print(new_string.capitalize())
print(f"Hello, {(new_string.capitalize())}!")

print("length of name --> ", len(new_string))

new_string_slice = (new_string.capitalize())
print("reversed name --> ", new_string_slice[::-1])