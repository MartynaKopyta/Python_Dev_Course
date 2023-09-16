# check for duplicates in the list:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
checked = []
duplicates = []
for i in some_list:
    for letter in checked:
        if i == letter:
            duplicates.append(i)
        else:
            continue
    checked.append(i)
print(duplicates)

# solution from the video using method count(), shorter
duplicates1 = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates1:
            duplicates1.append(value)
print(duplicates1)
