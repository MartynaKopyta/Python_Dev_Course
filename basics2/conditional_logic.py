# IF
is_old = False
is_licensed = False
# colon and indentation are important
if is_old and is_licensed:
    print('you can drive')
# elif is_licensed:   can be many elif statements
#   print('you can drive now')
else:
    print('you cannot drive')

# Truthy and Falsy
# if the variables given to if are not booleans, they automatically get converted to them
print(bool('hello'))  # Truthy values
print(bool(0))  # Falsy value
# if we ran bool conversion on it, and it's true -> truthy, similarly with false -> falsy

password = '123'
username = 'john'

if password and username:
    print('trying to log in')

# Ternary operator = conditional expression
# value_if_true if condition else value_if_false
is_user_friend = True
can_message = 'message allowed' if is_user_friend else 'not allowed to message'
print(can_message)


# Short-circuiting
is_friend = True
is_user = True
if is_friend or is_user:
    print('something')
# or is quicker because when it finds the first True, python stops
# with and in some condition it will stop but until something is False it has to check everything

# LOGICAL OPERATORS
# or, and, not, >, <, ==, >=, <=, !=
print(not True)

# exercise
is_magician = True
is_expert = True
# check if magician AND expert -> print('you are a master magician')
print('you are a master magician' if is_magician and is_expert else 'not a master yet')
# check if magician but not expert -> print('at least you are getting there')
print('at least you are getting there' if is_magician and not is_expert else 'okay')
# if not magician -> print('you need magic powers')
print('you need magic powers' if not is_magician else 'you are a magician')

# in one
if is_magician and is_expert:
    print('you are a master magician')
elif is_magician:
    print('at least you are getting there')
else:
    print('you need magic powers')

# is vs ==
print(True == 1)  # 1 truthy, so true
print('' == 1)  # '' falsy
print([] == 1)  # [] falsy
print(10 == 10.0)  # expected
print([] == [])  # empty list is empty list or falsy is falsy
# == checks equality of value

# is checks if the space in memory is the same
print(True is 1)  # false, True is True
print('' is 1)  # false, '1' is '1'
print([] is [])  # new locations, false
print(10 is 10.0)  # false, 10 is 10

a = [1, 2]
b = [1, 2]
print(a is b)  # false
print(a == b)  # true
