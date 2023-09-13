# General rules in python
# snake_case -> all lowercase + underscores
# start with lowercase or underscore
# case-sensitive -> num_1 != nuM_1
# can't overwrite keywords

user_iq = 190
print(user_iq)

user_sth = user_iq/4
print(user_sth)

# Constants convention -> capital letters
PI = 3.14

# Dunder starts with 2 underscores
# you can start variable with __ but convention is you shouldn't

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

# Expressions vs statements
iq = 100  # this line (and another) is a statement, performing an action
user_age = iq / 5  # iq / 5 -> expression, meaning it produces a value

# Augmented operator
some_value = 5
some_value += 2  # etc
print(some_value)
