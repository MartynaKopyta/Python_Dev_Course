class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):  # wizard extends user
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.num_arrows = num_arrows
        self.name = name

    def check_arrows(self):
        print(f'{self.num_arrows} arrows remaining')

    def run(self):
        print('ran really fast')


class HybridBorg(Wizard, Archer):  # multiple inheritance, order matters - beware of the constructor

    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


h1 = HybridBorg('Borgie', 50, 100)
h1.run()
h1.check_arrows()
h1.attack()
h1.sign_in()
# code gets really complex, be cautious and probably avoid
