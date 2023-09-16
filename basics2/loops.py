# Iterable - something that is able to get looped over
# FOR LOOPS
# for sth in Iterable:
#    ...

for item in 'Zero to Mastery':
    print(item)

for item in [1, 2, 3]:  # works with lists, sets, tuples
    print(item)
print(item)  # still works, prints 3

# my own example for dictionary, looping over keys - names
pet_owners = {'Anna': 'cat', 'John': 'dog'}
for i in pet_owners.keys():  # goes over keys anyway if just left as pet_owners
    print(i + ' has a ' + pet_owners.get(i))

for i in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c']:
        print(i, x)  # first takes 1, prints with a, b, c, escapes the inner loop to get to prints it with letters etc…

# more about ITERABLES
# iterable - list, dictionary, tuple, set, string
# iterated - one by one check each item in the collection

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for i in user.items():  # returning tuple
    print(i)

for key, value in user.items():  # returning key value
    print(key, value)

for i in user.values():
    print(i)

for i in user.keys():
    print(i)

# range() function
print(range(100))

for num in range(1, 11, 2):  # last argument - step, from 1 to 10 every second number
    print(num)

for _ in range(10):  # used to indicate that the loop variable doesn't matter,
    # we are just looping 10 times for example and that's what matters
    print(_)

for _ in range(10, 0, -1):  # goes in the opposite direction, can do step with -2, -3 etc
    print(_)

for i in range(2):
    print(list(range(10)))

# enumerate() function - takes an iterable object, when you need a counter
for i, char in enumerate('Helloo'):  # return the item of the iterable object with its INDEX
    print(i, char)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is {i}')

# WHILE LOOPS
# while condition:
#    ...

i = 0
while i < 5:
    print(i)
    # break stops the loop
    i += 1
else:  # when while is false, if the loop is broken in the while block, this else block won't be executed
    print('done with all the work')

# the same result in both loops:
my_list = [1, 2, 3]
for i in my_list:
    print(i)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
# for is simpler and better if we know how many times to loop, not sure - while is better

while True:
    print('say bye if you don\'t want to talk anymore')
    response = input('say something: ')
    if response.lower() == 'bye':
        break

# break, continue, pass
# break exits the loop
# continue stops the current iteration, python goes on to the next one
for i in my_list:
    if i == 2:
        continue
    print(i)
# pass just passes in the next line, may be useful if we don't know what to do yet
for i in my_list:
    pass  # nothing done but no error
