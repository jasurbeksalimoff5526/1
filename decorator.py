#1

'''
def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"funskiya nomi: {func.__name__}")
        print(f"argumentlar: args={args} kwargs={kwargs}")

        return func(*args, **kwargs)
    return wrapper

@decorator
def birnima(*args, **kwargs):
    print(sum(args) + sum(kwargs.values()))

birnima(1, 2, 3, a=10, b=15)
'''

#2

'''
def decorator(func):
    counter = 0
    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(f"funksiya {counter}-marta chaqirildi")

        return func(*args, **kwargs)
    return wrapper

@decorator
def test(*args, **kwargs):
    pass

test(1, 2, 3)
test("a")
test("b")
'''

#3

'''
user1 = {
    "name": "Ali",
    "is_logged": True
}

user2 = {
    "name": "Vali",
    "is_logged": False
}

def require_login(func):
    def wrapper(*args, **kwargs):
        user = args[0]
        if user["is_logged"] == True:
            return func(*args, **kwargs)
        else:
            print("ERROR")
    return wrapper

@require_login
def view_profile(user):
    print(f"Profile of {user}")


view_profile(user1)
view_profile(user2)
'''

#4

'''
def string(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return str(result)
    return wrapper

@string
def multiply(a, b):
    return a * b

print(multiply(5, 7))
'''

#5

'''
def write_log(func):
    def wrapper(*args, **kwargs):
        with open("log.txt", "a+") as f:
            f.write(f"{func.__name__} funksiyasi chaqirildi\n")

        return func(*args, **kwargs)
    return wrapper

@write_log
def multiply(a, b):
    print(a * b)

multiply(5, 7)
'''

#6

'''
def write_log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("natija.txt", "a+") as f:
            f.write(f"{func.__name__}: {result}\n")

        return result
    return wrapper

@write_log
def multiply(a, b):
    return a * b

print(multiply(5, 7))
'''
