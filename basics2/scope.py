# Scope means what variables I have access to
# If python doesn't have access to a variable it is going to throw an error

# global scope

def some_func():
    total = 100  # only in this block of code, local scope


if True:
    x = 10  # this var will still be visible outside if

print(x)

# scope is like a new word we create, so the variables declared inside
# a function declaration are not visible outside of it

# scope rules
a = 1


def confusion():
    a = 5
    return a


print(a)  # 1
print(confusion())  # 5

print(confusion())  # 5
print(a)  # 1 still, because a from the function does not have global scope

# 1 - start with local
# 2 - is there a parent scope?
# 3 - global
# 4 - built-in python functions


def parent():
    def confusion1():
        a = 10  # if it wasn't here then there is no a local, not in the parent, so python would go with global a
        return a
    return confusion1()


print(parent())
print(a)


def parent1():
    def confusion2():
        return sum  # no sum value in #1, #2, #3 so python is using a built-in function to avoid an error
    return confusion2()


print(parent1())

# parameters are local variables
# global keyword
total = 0


def count():
    global total  # keyword global says we want to use a global var
    total += 1
    return total


count()
count()
print(count())
# considered not a good practise, better dependency injection

total1 = 0


def count1(total1):
    total1 += 1
    return total1


print(count1(count1(count1(total1))))  # didn't have to use the keyword

# nonlocal keyword


def outer():
    b = 'local'

    def inner():
        nonlocal b  # it's saying that I want to use a var from outside the current scope
        b = 'nonlocal'  # changing the 'local' b to sat 'nonlocal',
        # without this line outer() would still have b = 'local'
        print('inner:', b)
    inner()
    print('outer:', b)


outer()
# Why do we need scope?
# to use resources efficiently, to use less memory
# for example python will automatically get rid of variables from a function execution because it is done with them
