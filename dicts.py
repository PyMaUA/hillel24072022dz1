ascii_table = {element: chr(element) for element in range(128)}
print(ascii_table)

##################################################################

import string

alphabet = {
    letter: index
    for index, letter in enumerate(string.ascii_lowercase)
}
print(alphabet)

password = int(
    input("Type positive integer value for password: ")
) % len(alphabet)

alphabet_secure = {
   index - password + (len(alphabet) if password > index else 0): letter
    for letter, index in alphabet.items()
}
print(alphabet_secure)

text_to_encode = input("Type text to encode without spaces: ")
encoded_text = "".join(
    [alphabet_secure[alphabet[letter]]
     for letter in text_to_encode]
)
print(encoded_text)





# import string
#
# alphabet = {index: element for index, element in enumerate(string.ascii_lowercase)}
# print(alphabet)
