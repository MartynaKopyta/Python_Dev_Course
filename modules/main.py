import utility
from shopping import shopping_cart
# import random
# or we can be more explicit with the import statement  
from random import shuffle
# or import shopping.shopping_cart

def main():
    print(utility.multiply(10, 2))
    cart = shopping_cart.buy("apple")
    print(cart)
    cart = shopping_cart.buy_anything(cart)
    shuffle(cart) # Example of random module use - shuffle a list
    print(cart)

if __name__ == "__main__":
    main()

'''
Other useful built-in modules:
- sys - ex. sys.argv it allows as to pass arguments to the script from the command line. 
For example we can have a python file script.py with content  like this:
import sys
first = sys.argv[1] # we start from one, cause the first argument is the name of the script
second = sys.argv[2]
print(f'Hi {first} {second}')

And we can run it from the command line like this:
python script.py John Doe
'''