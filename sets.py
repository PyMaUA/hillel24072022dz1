set_1 = set(input("Please enter a set of characters "))
set_2 = set(input("Please enter yet another set of characters "))

set_letters = set_1.intersection(set_2)
set_letters = {element for element in set_letters if element.isalpha()}

set_digits = set_1.symmetric_difference(set_2)
set_digits  = {element for element in set_digits if element.isdigit()}

print(f"{set_letters=}")
print(f"{set_digits=}")

#############################################

set_a = {1, 3, 5, 7, 9}
set_b = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
set_c = {"s", "f", "U", "R", "r", "j", 5, 7}
print(f"union --> {set_a | set_b | set_c}")
print(f"intersection --> {set_a & set_b & set_c}")
print(f"difference --> {set_b - set_c - set_a}")
print(f"symetric_difference --> {set_a ^ set_b ^ set_c}")
