def log_call(func):
    def wrap(*args, **kwargs):
        print(f"Calling: {func.__name__}(args={args}, kwargs={kwargs})")
        res = func(*args, **kwargs)
        print(f"-> {res}")
    return wrap


@log_call
def add(a, b):
    return a + b


@log_call
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


add(3, 5)
greet("Luka", greeting="Hi")
