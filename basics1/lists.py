# List - ordered list of objects of any type
li = ['a', 1, True]
shopping_cart = ['notebook',
                 'sunglasses',
                 'toy',
                 'grapes']
print(shopping_cart[0])  # there is order

# List slicing
# same as with strings
print(shopping_cart[0:2])
print(shopping_cart[::2])
# but lists are mutable
shopping_cart[0] = 'cheese'
print(shopping_cart)
new_cart = shopping_cart[1:3]  # created a copy
print(new_cart)

# NOTE
new_cart = shopping_cart
new_cart[0] = 'gum'
print(new_cart)
print(shopping_cart)
# works like this because we are not copying the original list
# TO COPY DO THIS:
shopping_cart1 = ['butter',
                  'milk',
                  'honey']
new_cart1 = shopping_cart1[:]  # THIS
new_cart1[0] = 'bread'
print(shopping_cart1)
print(new_cart1)

# MATRIX, two or more dimensions
matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]
# X represented in 0 and 1 now, often used in complex calculations
print(matrix[0])  # first row
print(matrix[0][1])  # second item of the first row

# LIST FUNCTIONS, METHODS
print(len(shopping_cart))

# adding
shopping_cart.append(100)
# new_list = shopping_cart.append(100) will result in None when printed
# because it modifies the list in place, does not however produce a value
new_list = shopping_cart
print(new_list)
print(shopping_cart)

# inserting, same about modifying not copying
shopping_cart.insert(3, 'mango')
print(shopping_cart)

# extend takes iterable
new_list = shopping_cart.extend([100, 101])  # extends by a list
print(new_list)
print(shopping_cart)

# removing
shopping_cart.pop()  # removes the last item
print(shopping_cart)
cart1 = shopping_cart.pop(1)  # removes item at the given index, returns the popped value
print(shopping_cart)
print(cart1)
cart2 = shopping_cart.remove('toy')  # only changes in the list, no value
print(shopping_cart)
print(cart2)
# remove changes in place, pop can produce a value
cart3 = shopping_cart.clear()
print(shopping_cart)
print(cart3)

# index
basket = ['a', 'x', 'b', 'c', 'd', 'e']
print(basket.index('b'))  # where is b
# optional parameters, where should you start looking start, stop
print(basket.index('d', 2, 5))

# key word 'in'
print('b' in basket)  # returns bool
print('i' in 'inna')

# key word 'count
print(basket.count('b'))  # how many b's are in the list

# sorting
# basket.sort() modifies in place
print(sorted(basket))  # copies and sorts, new list produced
print(basket)  # original basket remains unchanged
# sorted works same as
new_basket = basket[:]
new_basket.sort()
print(new_basket)
print(basket)
# instead of basket[:] to copy, you can do basket.copy()

basket.reverse()  # switching indexes, not reverse sorting
print(basket)

# LIST PATTERNS
# len ...
basket.sort()
basket.reverse()
print(basket[::-1])  # slicing creates a new list
print(basket)
# range - generate a list for example
list1 = list(range(1, 10))
print(list)
# .join() joins items in a list by whatever is in join(HERE)
sentence = ' '
new_sentence = sentence.join(['hi', 'Andy'])
print(sentence)
print(new_sentence)
print(' '.join(['hi', 'Andy']))

# list unpacking
num1, num2, num3, *other, num4 = [1, 2, 3, 4, 5, 6, 7, 8]
print(num3)
print(other)
print(num4)
