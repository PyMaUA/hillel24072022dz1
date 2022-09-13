## task_1
def sum(num_start: int, num_end: int):

    if num_end > num_start:
        num_start, num_end == num_end, num_start

    result = 0
    for element in range(num_start, num_end+1):
        result += element
    return result

num_start = 2
num_end = 24
print(f"sum=", sum(num_start, num_end))

#_task_2_##################################################

def happy_time(seconds):

    DAY = 60 * 60 * 24
    HOUR = 60 * 60
    MINUTE = 60

    result_days = seconds // DAY
    result_hours = seconds % DAY // HOUR
    result_minutes = seconds % DAY % HOUR // MINUTE
    result_seconds = seconds % DAY % HOUR % MINUTE

    print(
        f"{result_days=}, "
        f"{result_hours=}, "
        f"{result_minutes=}, "
        f"{result_seconds=}, "
    )
    return (result_days, result_hours, result_minutes , result_seconds)

seconds = 10000
print(f"happy_time=", happy_time(seconds))

##_task_3_##################################################

#_for_cycle
def my_sum(numlist):

    result = 0
    for element in numlist:
        result += element
    return result

numlist = [2,5,33,6,58,3,26]
print(f"sum=", my_sum(numlist))

#_while_cycle
def my_sum_1 (numlist_1):
    result = 0
    while numlist_1:
        result += numlist_1.pop()

    return result

numlist_1 = [2, 5, 33, 6, 58, 3, 26]
print(f"sum=", my_sum_1(numlist_1))

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