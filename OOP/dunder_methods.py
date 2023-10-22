# dunder methods - inherited from base object class

class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {'name': 'Yoyo', 'has_pets': False}

    def __str__(self):  # can be modified if needed for example to print comfortably
        return f'{self.color}'

    def __len__(self):
        return self.age

    def __del__(self):
        print('deleted')

    def __call__(self):
        return 'yes?'

    def __getitem__(self, item):
        return self.my_dict[item]


action_figure = Toy('red', 2)
print(action_figure.__str__())
print(str(action_figure))  # __str__
print(action_figure)
print(len(action_figure))
print(action_figure())  # __call__ related ()
print(action_figure['name'])  # __getitem__ related []
del action_figure  # __del__
