# no name, anonymous functions used just once
print(list(map(lambda item: item * 2, [1, 2, 3])))

print(list(filter(lambda item: item % 2 == 0, [1, 2, 3, 4])))

# square list
l1 = [5, 4, 3]
print(list(map(lambda item: item**2, l1)))

# list sorting byt the second value
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda item: item[1])
print(a)
