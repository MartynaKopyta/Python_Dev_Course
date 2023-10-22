# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
c1 = Cat('Bob', 2)
c2 = Cat('Puss', 1)
c3 = Cat('Chloe', 5)


# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {oldest_cat(c1.age, c2.age, c3.age)} years old.')
