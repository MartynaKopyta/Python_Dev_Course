# Age guessing
birth_year = input('What year were you born? ')
age = 2023 - int(birth_year)
print('You are ' + str(age) + ' years old!')

# age = 2019 - bool(birth_year) would result in 2018, cause True is 1
