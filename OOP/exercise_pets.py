class Pets:
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Filemon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 1 Add another Cat

# 2 Create a list of all the pets (create 3 cat instances from the above)
si = Simon('Simon', 11)
sa = Sally('Sally', 5)
fi = Filemon('Filemon', 3)
my_cats = [si, sa, fi]

# could also use
# my_cats = [Simon('Simon', 11), Sally('Sally', 5), Filemon('Filemon', 3)]

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

# 4 Output all the cats walking using the my_pets instance
my_pets.walk()
