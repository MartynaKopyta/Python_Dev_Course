# when zero - display empty space in the terminal, one - *
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for line in picture:
    row = ''
    for number in line:
        if number == 0:
            row += ' '
        else:
            row += '*'
    print(row)

# fill = '*'
# empty = ' '
# using parameter of print function
for line in picture:
    for number in line:
        if number == 0:  # if number
            print(' ', end='')  # no new line, could change to empty
        else:
            print('*', end='')  # could change to fill
    print('')  # new line by default

# GOOD CODE:
# clean - readable, no extra stuff, well formatted
# readable - meaningful names, comments when needed
# predictability - not about being the most clever
# DRY - don't repeat yourself

# in comments in the second for loop are some ideas about cleaning the code
# in this case it makes it more complicated, imagining it was much more complex, could be useful, more flexible
