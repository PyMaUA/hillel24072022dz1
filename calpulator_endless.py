while True:
    num_1 = input("Please enter a value ")
    if num_1 == "exit":
        break
    num_2 = input("Please enter a value ")
    if num_2 == "exit":
        break
    action = input("Please enter an arithmetic operation ")
    if action == "exit":
        break
    value = num_1
    print("number order num_1 --> ", len(str(num_1).split(".")[0]))
    value = num_2
    print("number order num_2 --> ", len(str(num_2).split(".")[0]))


    if "." in num_1:
        num_1 = float(num_1)
    else:
        num_1 = int(num_1)
    print(f"{num_1}", type(num_1))

    if "." in num_2:
        num_2 = float(num_2)
    else:
        num_2 = int(num_2)
    print(f"{num_2}", type(num_2))

    if action == "+":
        result = num_1 + num_2
        print(f"{result}", type(result))

    elif action == "-":
        result = num_1 - num_2
        print(f"{result}", type(result))

    elif action == "*":
        result = num_1 * num_2
        print(f"{result}", type(result))

    elif action == "/":
        try:
            result = num_1 / num_2
            print(f"{result}", type(result))
        except ZeroDivisionError:
            print("You can't dividing on zero")

    elif action == "**":
        result = num_1 ** num_2
        print(f"{result}", type(result))

    else:
        print("Sorry, the action was entered incorrectly...")


    if num_1 >= num_2:
        result = num_1 >= num_2
        print(f"{result}")
    if num_1 <= num_2:
        result = num_1 <= num_2
        print(f"{result}")
