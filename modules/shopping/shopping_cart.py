import random

def buy(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

def buy_anything(cart=None):
    # Example of random module use - random choice from a list
    random_items = ["banana", "cherry", "date", "elderberry"]
    if cart is None:
        cart = []
    cart.append(random.choice(random_items))
    return cart