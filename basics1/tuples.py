# Tuple - lists but immutable
my_tuple = (1, 2, 3, 4, 5, 5)
# my_tuple[1] = 'z' won't work because of the immutability

print(my_tuple[1])
print(my_tuple)
print(5 in my_tuple)

# why do you need this if it works like a list except immutable?
# tells other programmers that this is not to be changed, it's safer
# usually faster than a list, so if we don't need a list to change, tuple is better

# a tuple can be a key in a dictionary
user = {
    (1, 2): [1, 2, 3],
    'a': 2
}
print(user[(1, 2)][1])

# slicing
new_tuple = my_tuple[1:2]
print(new_tuple)
x, y, z, *other = my_tuple
print(other)

print(my_tuple.count(5))  # how many fives
print(my_tuple.index(5))  # index of the first five
print(len(my_tuple))  # works 
