# Dictionary (dict), {key : value .. } - unordered key, value pair,
# each pair can be in different space of the memory, not next to each other as in lists
dictionary = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
}
print(dictionary['b'])  # access objects by their key
print(dictionary)  # the pairs may not be returned in the original order so again, unordered
print(dictionary['a'][1])

# Dictionary can be a part of a list for example
my_list = [{
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
},
    {
        'a': [4, 5, 6],
        'b': 'bye',
        'x': False
    }
]
print(my_list[1]['a'][0])

dictionary1 = {
    123: [1, 2, 3],
    True: 'hello',
    # [123]: True - won't work, key cannot change and list is mutable therefore can't be a key
    (1, 2): 'a'   # a tuple can be a key as it is immutable
}
# keys need to be unique, if keys have the same names there is no error
# but that is because the value assigned to a key was overridden

# METHODS
user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}
print(user.get('age'))  # you can check if something is in a dict without an error, opposed to user['age']
print(user.get('age', 55))  # grab age, if it doesn't exist say its 55 by default

# another, not preferred way, to create a  dictionary
user2 = dict(name='John')
print(user2)

# same as in lists, keyword 'in' can be used if a dict contains a key
print('basket' in user)

print('size' in user.keys())  # checks keys
print('hello' in user.values())  # checks values
print(user.items())  # grabs pairs

user2 = user.copy()
print(user2)
print(user.clear())  # won't return a value, works in place
# user2 is not empty now, because it copied the original, it wasn't said to be equal to it
print(user)

print(user2.pop('age'))
print(user2)
print(user2.popitem())  # pops something randomly
print(user2)

print(user2.update({'age': 55}))
print(user2.update({'ages': 55}))  # takes a dictionary as an argument, if key doesn't yet exist, new pair is added
print(user2)
