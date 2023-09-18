def say_hello():
    print('hello')


say_hello()
say_hello()  # no redundant code

# arguments vs parameters

# parameters in the brackets in the function definition
# positional parameters - position matters


def say_hellooo(name, emoji):
    print(f'Hellooo {name} {emoji}')


# arguments, actual value given while calling / invoking the function
# positional arguments - position in which given matters
say_hellooo('Mary', ':)')
say_hellooo('Dan', ';)')

# keyword arguments - might be a bad practise, why wouldn't you just follow the function to make it simpler
say_hellooo(emoji=':)', name='Bibi')

# default parameters - function still works when not given arguments because there are the default ones


def say_henlo(name='Darth Vader', emoji=':)'):
    print(f'Henlo {name} {emoji}')


say_henlo()
say_henlo('Brad', ':(')
# return keyword


def sum1(num1, num2):
    return num1 + num2


print(sum1(1, 2))
# in general function either modifies something or returns something
# should do one thing really well, usually return something

print(sum1(10, sum1(10, 5)))


def sum2(num1, num2):
    def another_funct(n1, n2):
        return n1 + n2
    return another_funct(num1, num2)  # without this we are only defining the function and returning nothing at all


print(sum2(10, 5))
# this function is not very clear but shows the idea of how returning works
# return exits the function, whatever is after return won't get executed

# methods vs functions
# methods are owned by objects, functions are accessible without an object

# Docstrings allow us to add info about defined functions


def test(a):
    """
    This function tests and prints param a
    :param a: is printed
    :return: None
    """
    print(a)


test('!!!')  # docstring shows on hover
help(test)  # prints the docstring
print(test.__doc__)  # same usage

# clean code


def is_even(num):
    return num % 2 == 0


print(is_even(50))

# *args **kwargs
# arguments, keyword arguments


def super_func(name, *args, i='hi', **kwargs):  # the star makes the function accept any given number of arguments
    total = 0
    for items in kwargs.values():  # kwargs are given as a dictionary, so we have to get to its values
        total += items
    return sum(args) + total


print(super_func('Andy', 1, 2, 3, num1=5, num2=10))

# rule: params, *args, default parameters, **kargs