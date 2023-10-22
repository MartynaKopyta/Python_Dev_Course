class User:

    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):  # wizard extends user
    def __init__(self, name, power, email):
        super().__init__(email)  # could also be User.__init__(self, email) - self needed in this case
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.num_arrows = num_arrows
        self.name = name

    def attack(self):
        # User.attack(self)
        print(f'attacking with {self.num_arrows} arrows')


wizard1 = Wizard('Merlin', 50, 'meril@gmail.com')
archer1 = Archer('Robin', 100, 'robin@gmail.com')

wizard1.sign_in()
archer1.sign_in()

wizard1.attack()
archer1.attack()

# to check if sth is an instance of a class
print(isinstance(archer1, User))
# parent of every class - object class
print(isinstance(archer1, object))


def player_attack(character):  # example of polymorphism - different output for different objects
    character.attack()


player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:  # another example
    char.attack()

wizard1.attack()  # wizard overrides the original method from its super class

print(wizard1.email)

# introspection - when the code is running you can determine the type of object
print(dir(wizard1))  # shows all methods and attributes
