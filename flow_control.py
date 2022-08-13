num_1 = input("Please enter a value ")
num_2 = input("Please enter a value ")
action = input("Please enter an arithmetic operation ")

print("number order num_1 --> ", len(num_1))
print("number order num_2 --> ", len(num_2))

match action:
    case "+":
        print("OK")
    case "-":
        print("OK")
    case "*":
        print("OK")
    case "/":
        print("OK")
    case "**":
        print("OK")
    case _:
        print("Sorry, the action was entered incorrectly...")

try:
    num_1 = int(num_1)
except ValueError:
    num_1 = float(num_1)
print(f"{num_1}", type(num_1))

try:
    num_2 = int(num_2)
except ValueError:
    num_2 = float(num_2)
print(f"{num_2}", type(num_2))


if action == "+":
    result = num_1 + num_2
    print(f"{result}", type(result))

if action == "-":
    result = num_1 - num_2
    print(f"{result}", type(result))

if action == "*":
    result = num_1 * num_2
    print(f"{result}", type(result))

if action == "/":
    try:
        result = num_1 / num_2
        print(f"{result}", type(result))
    except ZeroDivisionError:
        print("You can't dividing on zero")

if action == "**":
    result = num_1 ** num_2
    print(f"{result}", type(result))

if num_1 >= num_2:
    result = num_1 >= num_2
    print(f"{result}")
if num_1 <= num_2:
    result = num_1 <= num_2
    print(f"{result}")
