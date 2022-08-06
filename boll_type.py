# 3 ! 5
comparison_result: bool = 3 != 5
print(comparison_result)

comparison_result: bool = 3 < 5
print(comparison_result)

# 5_5
value_true = True

comparison_result: bool = 5 == 5
print(comparison_result)

x = 5
y = x
is_ident = x is y
print(is_ident)

# or, and, not
is_true_1 = True or (True and False)
print(f"{is_true_1=}")

is_true_2 = True and (True or False)
print(f"{is_true_2=}")

is_true_3 = (True and True) or False
print(f"{is_true_3=}")

is_true_4 = (True or True) or False
print(f"{is_true_4=}")

is_true_5 = not True or (True or False)
print(f"{is_true_5=}")

# comparison_bool

comparison_result: bool = bool(None) < bool(7)
print(comparison_result)

comparison_result_1: bool = bool("") < bool(10 - 1)
print(comparison_result_1)

one_space_str = bool("Hello") or bool("True or False")
print(f"{one_space_str=}")

none_obj = None
print(type(none_obj), none_obj)
variable = type(none_obj)

x = None
y = x
is_ident = x is y
print(is_ident)
print(id(x), id(y))