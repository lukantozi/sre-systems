# Task 1
def loop_my(n):
    total = 0
    if n == 0:
        return total
    elif n < 0:
        return f"please enter positive value"
    for i in range(1, n + 1):
        total += i
    return total
#print(loop_my(5))
#print(loop_my(100))

# Task 2
def digits_my(n):
    if n == 0:
        return 0
    elif n < 0:
        return "please enter positive value"
    mult = 1

    while n != 0:
        fact = n % 10
        mult *= fact
        n //= 10

    return mult
#print(digits_my(234))

# Task 3
def strings_my(s):
    vow = ["a", "e", "i", "o", "u"]
    vow_num = 0
    for char in s:
        if char.lower() in vow:
            vow_num += 1
    return vow_num
#print(strings_my("Hello World"))
#print(strings_my("python"))

# Task 4
def commands_my():
    list_f = []

    commands = {
            "append": lambda x: list_f.append(float(x[0])),
            "max": lambda x: print(max(list_f)),
            "min": lambda x: print(min(list_f)),
            "remove": lambda x: list_f.remove(float(x[0])),
            "insert": lambda x: list_f.insert(int(x[0]), float(x[1])),
            "pop": lambda x: list_f.pop(),
            "sort": lambda x: list_f.sort(),
            "reverse": lambda x: list_f.reverse(),
            "print": lambda x: print(list_f),
            }

    n = int(input())
    for _ in range(n):
        command = input().split()
        oper = command[0]
        vals = tuple(command[1:])
        commands[oper](vals)

#commands_my()

# Task 5
def dict_my(d):
    d_copy = d.copy()
    for key, value in d_copy.items():
        if not (isinstance(value, int) or isinstance(value, float)):
            d.pop(key)
    del d_copy
    return d
#print(dict_my({"name": "Alice", "age": 30, "score": 95.5, "city": None}))

# Task 6
def set_my(s_1, s_2):
    return s_1 - s_2

#set_1 = {1, 2, 3, 4, 5, 6, 7,}
#set_2 = {3, 4, 5, 6, 7, 8, 9,}
#print(set_my(set_1, set_2))

# Task 7
def split_join(s):
    words = s.split()
    words = [f"{word}-{word}" for word in words]
    return " ".join(words)
#print(split_join("hello world"))
