"""
Decorators look like this for example @classmethod, @staticmethod, @property
Decorators are used to modify the behavior of functions or methods.
Side note: higher order functions are functions that take other functions as arguments or return them as results.
Decorators are a form of higher order functions.
"""
"""
Decorators look like this for example @classmethod, @staticmethod, @property
Decorators are used to modify the behavior of functions or methods.
Side note: higher order functions are functions that take other functions as arguments or return them as results.
Decorators are a form of higher order functions.
"""

def print_stars(func):
    def wrapper():
        print("**********")
        func()
        print("**********")
    return wrapper

def print_dashes(func):
    def wrapper():
        print("----------")
        func()
        print("----------")
    return wrapper

@print_dashes
@print_stars
def say_hello():
    print("Hello!")

say_hello()
print("\n")
# Equivalently we can do this:
# say_hello = print_dashes(print_stars(say_hello))
# say_hello()

# Another example

def my_decorator(func):
    '''
    We use *args and **kwargs to accept any number of positional and keyword arguments
    '''
    def wrapper(*args, **kwargs):
        print("*************")
        func(*args, **kwargs)
        print("*************")
    return wrapper

@my_decorator
def say_hello(name, surname, age, emoji=":)"):
    print(f"Hello {name} {surname} age {age} {emoji}")

say_hello("John", "Smith", 11)