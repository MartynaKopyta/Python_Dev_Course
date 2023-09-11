# Strings
username = "name"
password = "password"
long_string = '''
WOW
___
'''
print(long_string)

first_name = 'John'
last_name = 'Smith'
full_name = first_name + ' ' + last_name
print(full_name)

# concatenation - adding strings
print('Hello ' + first_name)

# TYPE CONVERSION
print(type(str(100)))  # is string
# int(..), str(..) etc.

a = str(100)
b = int(a)
c = type(b)
print(c)

# escape sequence - whatever comes after backslash is a string
weather1 = 'it\'s sunny'
weather2 = "it's kinda sunny"
weather3 = 'it\'s "kinda" sunny'
weather4 = "\tit\\s 'kinda' sunny\n hello"  # \t adding tab, \n new line
print(f'{weather1} = {weather2} = {weather3} = {weather4}')

# formatted strings
age = 55
print('Hi ' + first_name + '! You are ' + str(age) + " years old.")
print(f'Hi {first_name}! You are {age} years old.')
# before python 3, if args in order you can skip numbers in {}, if you create vars in format(..) put their names in {}
print('Hi {1}! You are {0} years old.'.format(first_name, age))

# string indexes, slicing
selfish = 'me me me'
print(selfish[0])
# [start:stop]
print(selfish[0:4])
# stopover [0:8:2] by two here
print(selfish[0:8:2])
# [1:] from second to the end, [:5] to fifth
# [::1] default, whole string
# [-1] the last one, counts from the end
print(selfish[::-1])  # reverse of the string, [::-2] would be every other from the end

# immutability, if you want to change a string, you can only replace it
# for example can't change a single character from a string

# FUNCTIONS
# For type conversion str(), int() etc
print(float(5))
# For numbers round(), abs() etc
print(round(8.3))
# For strings len()
print(len('hellooo'))  # counts like a human from 0

# METHODS for Strings
quote = 'to be or not to be'
print(quote.upper())  # lower similarly
print(quote.capitalize())  # Only the first letter
print(quote.find('be'))  # be is first found at index 3
print(quote.replace('be', 'me'))
