# print the highest even of the list
def highest_even1(numbers):
    highest = 0
    for num in numbers:
        if num % 2 != 0:
            continue
        if num > highest:
            highest = num
    return highest


print(highest_even1([10, 2, 3, 4, 8, 11]))

# solution from the video:


def highest_even2(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even2([10, 2, 3, 4, 8, 11]))
