# Ctrl / - multiple line comment

name = input("What is your name? ")
print("Hello " + name + " !")
print("Hello", name, "!")

# Data Types:
# int
# float
# bool
# str
# list
# tuple
# set
# dict

# check type
print(type(2 + 4))
print(type(2 / 4))

# Classes -> custom types

# Specialized Data Types -> packages, modules

# None = Null

# Operators apart from the obvious:
# 2 to the power of 3
print(2 ** 3)
# 5 divided to 4 and rounded to an integer
print(5 // 4)
# remainder of this devision
print(5 % 4)

# Math functions
print(round(3.1))
print(abs(-20)) #absolute value

# Operator precendence - usuall math rules apply
# () -> ** -> * / -> + -

# Extra data type - complex, for complex math

# bin - returns binary representation of an integer
print(bin(5))  # in python all start with 0b and then the binary number
print(int('0b101', 2))  # base 2 - binary numer given

# booleans
name = 'Andy'
is_cool = False
print(bool(1))  # True
print(bool(0))  # False
print(bool('True'))  # Valid bool
