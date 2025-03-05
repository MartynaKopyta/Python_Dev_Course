class Hero():

    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self):
        target_name = input('Who do you want to attack? ')
        if target_name == self.name:
            print('You cannot attack yourself! Try again!')
            return self.attack()
        print(f'{self.name} is attacking {target_name}.')
        return target_name, self.power

    def __str__(self):
        return f'{self.name} has {self.health} health and {self.power} power.'
    
    def takeDamage(self, damage):
        self.health -= damage

    def checkHealth(self):
        return self.health
    

class GameEngine():

    heroes = []
    number_of_heroes = 0
    num_of_rounds = 15

    def __init__(self, number_of_heroes):
        self.number_of_heroes = number_of_heroes

    def add_heros(self):
        for i in range(self.number_of_heroes):
            try:
                name = input(f'Enter {i + 1} hero name: ')
                health = input(f'Enter {i + 1} hero health: ')
                power = input(f'Enter {i + 1} hero attack power: ')
                self.heroes.append(Hero(name, int(health), int(power)))
            except ValueError:
                print('Please enter a valid number for health and power.')
                self.add_heros()

    def introduce_heroes(self):
        print('-----------------------------------')
        for hero in self.heroes:
            print(hero)
        print('-----------------------------------')

    def start_game(self):
        for i in range(self.num_of_rounds):
            for hero in self.heroes:
                print(f'{hero.name} is now playing...')
                name_to_attack, power_to_attack = hero.attack()
                self.attackGivenHero(name_to_attack, power_to_attack)
                print('-----------------------------------')
                if len(self.heroes) == 1:
                    print(f'{self.heroes[0].name} has won the game!')
                    self.end_game()
            if i % len(self.heroes) == 0:
                self.introduce_heroes()

    def attackGivenHero(self, name, yourPower):
        for hero in self.heroes:
            if hero.name == name:
                hero.takeDamage(yourPower)
                print(f'{name} is taking {yourPower} damage!')
                if hero.checkHealth() <= 0:
                    print(f'{name} has died!')
                    self.heroes.remove(hero)
                break
        else:
            print('No hero with that name found. Try again next time...')

    def end_game(self):
        print('Game Over!')
        exit()

def main():
    try:
        number_of_heroes = int(input('Enter number of heroes: '))
        game = GameEngine(number_of_heroes)
        game.add_heros()
        game.introduce_heroes()
        game.start_game()
    except ValueError:
        print('Please enter a valid number.')
        main()

if __name__ == '__main__':
    main()