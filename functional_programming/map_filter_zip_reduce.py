from functools import reduce
# map - applies a function to given iterable data
my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


# map returns an object in the memory, turn into a list to view
# print(list(map(multiply_by2, [1, 2, 3])))
print(list(map(multiply_by2, my_list)))
print(my_list)  # no effect on the existing list, map is a pure function


# filter


def only_odd(i):
    return i % 2 != 0


# also applies action, finds True
print(list(filter(only_odd, [1, 2, 3])))

# zip - zipping iterables first items with first, second with second...
l1 = [1, 2, 3]
l2 = [10, 20, 30]

print(list(zip(l1, l2)))

usernames = ['Anna', 'Kot']
passwords = ['ania1', '123']
email = ['ania@gamil.com', 'kot@gmail.com']

print(list(zip(usernames, passwords, email)))

# reduce - reducing list to some sort of manipulated data


def accumulator(acc, item):  # first acc is the reduce last argument
    print(acc, item)
    return acc + item  # next pass acc it the output of this return


print(reduce(accumulator, my_list, 0))


def multi(mult, item):
    return mult * item


print(reduce(multi, [2, 3, 4], 1))
