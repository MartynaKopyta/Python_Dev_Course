class PlayerCharacter:
    # class object attribute - static
    membership = True

    def __init__(self, name, age=0):  # constructor, can use default parameters
        if self.membership:  # here redundant code, but could be useful to check some rules
            self._name = name  # no real private variables in python _ is used to signal that sth should be private
            self._age = age
# could also be PlayerCharacter.membership, this way we refer to class object attribute, PlayerCharacter.name won't work

    def run(self, how):
        print(f'{self._name} in running {how}')
        return 'done'

    # def __str__(self): makes printing PlayerCharacter print name
    #     return self.name

    @classmethod  # can be used without instantiating a class
    def adding_things(cls, num1, num2):  # 1 argument is standard
        return cls('Teddy', num1 + num2)  # with cls you can create objects here (optional)

    @staticmethod  # used when we don't care about the state of the object/class
    def adding(num1, num2):  # no cls
        return num1 + num2


player1 = PlayerCharacter('Adam', 23)
player2 = PlayerCharacter('Cindy', 24)

print(player1)
player1.run('fast')

# print(player2.name)
print(player2.run('slowly'))

player1.attack = 50
print(player1.attack)
# print(player2.attack) error

# help(player1)  # describes the class, applies to all objects (strings, lists etc.)

print(player1.adding_things(1, 1))
player3 = PlayerCharacter.adding_things(2, 3)  # using a class method
# print(player3.age)

# 4 Pillars of OOP
# encapsulation - functions and attributes encapsulated is a class - a package of those
# abstraction - hiding information, that is enabling access only to necessary data
# its abstracting away things we don't need to care about, the user doesn't need to know
# inheritance - parent - child idea, shared and extended functionality
# polymorphism - the same methods can be implemented many ways
