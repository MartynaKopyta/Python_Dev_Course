# Set - unordered collection of unique objects
my_set = {1, 2, 3, 4, 5, 5}
print(my_set)  # only returns unique items

my_set.add(100)
my_set.add(2)  # can't be added
print(my_set)

my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))  # you can return only unique items of a list by converting it to a set

# print(my_set[1]) won't work, no order
print(1 in my_set)
print(len(my_set))  # only counts unique, duplicates never get entered

new_set = my_set.copy()
my_set.clear()  # works in place
print(new_set)
print(my_set)

print(list(my_set))  # can be converted

# MORE METHODS
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8, 9, 10}

# comparing
print(set1.difference(set2))  # what set1 has that set2 doesn't
print(set1)  # not modified

print(set1.intersection(set2))  # what both set1 and set2 have
print(set1 & set2)  # same meaning, not used as often
print(set1)

print(set1.isdisjoint(set2))  # are the sets completely different, do they have nothing in common

print(set1.issubset(set2))  # is set1 a subset of set2
print(set1.issuperset(set2))  # is it a superset of set2

# removing items
print(set1.discard(5))  # no value returned
print(set1)  # set1 is now changed -  discard works in place

# remove from set1 elements that are also in set2
print(set1.difference_update(set2))  # again, just modifies
print(set1)  # unlike just difference, the set was changed

# united sets together, no duplicates
print(set1.union(set2))
print(set1 | set2)  # same meaning as the line above
