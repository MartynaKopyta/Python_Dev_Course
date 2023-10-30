# list, set, dictionary
# quick way to create an object without for loop

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# instead

# create a var, for each var in iterable add to list
my_list1 = [char for char in 'hello']
print(my_list1)

my_list2 = [num for num in range(0, 100)]
print(my_list2)

my_list3 = [num ** 2 for num in range(0, 10)]
print(my_list3)

my_list4 = [num for num in list(filter(lambda i: i % 2 == 0, my_list3))]
print(my_list4)

my_list5 = [num**2 for num in range(0, 10) if num % 2 == 0]
print(my_list5)

# for set same but changing the brackets

set1 = {num*2 for num in range(0, 3)}
print(set1)

simple_dict = {
    'a': 1,
    'b': 2
}
# dictionaries same but pairs
my_dict = {key: value*2 for key, value in simple_dict.items() if value % 2 == 0}
print(my_dict)

my_dict2 = {k: k**2 for k in [1, 2, 3]}
print(my_dict2)

# duplicate exercise
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list(set([num for num in some_list if some_list.count(num) > 1]))
# cast to set first to only keep unique values and then return to list
print(duplicates)
