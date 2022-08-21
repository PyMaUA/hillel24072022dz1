text_for_processing = input("Please enter text with numbers ")

collector_capital_letters = ""
collector_index_space = ""
collector_vowel_letters = ""
counter = 0

for index, symbol in enumerate(text_for_processing):
    if symbol.isupper():
        collector_capital_letters += symbol

    if symbol == " ":
        collector_index_space += str(index, ) + ","

    if symbol.lower() in "aeiuoyAEIUOY":
        collector_vowel_letters += symbol + ","

    if symbol.isdigit():
        counter += 1
        if counter == 3:
            print("loop break")
            break
    else:
        counter = 0
if counter != 3:
    print("loop is finished")

print(f"{collector_capital_letters = }")
print(f"{collector_index_space=}")
print(f"{collector_vowel_letters=}")