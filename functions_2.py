##_task_3_##################################################

#_factorial
def my_sum_2(numlist_2):

    if len(numlist_2) ==1:
        return numlist_2[0]
    else:
        return numlist_2[0] + my_sum_2(numlist_2[1:])

numlist_2 = [2,5,33,6,58,3,26]
print(f"sum=", my_sum_2(numlist_2))

##_task_4_##################################################

def fibonacci(n):
    a = 0
    b = 1
    for element in range(n):
        a, b = b, a + b
    return a
print(fibonacci(4)) # sequence number

##_or

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(4)) # sequence number


##_task_5_##################################################

def sandwich_decor(func_to_decor):
    print("Помідор")

    def warapper():
        print("М'ясо")
        func_to_decor()
        print("Хліб")

    return warapper

@sandwich_decor
def sandwich_func():
    print("Сир")

sandwich_func()