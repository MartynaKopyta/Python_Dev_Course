import utility
from shopping import shopping_cart
# or import shopping.shopping_cart

def main():
    print(utility.multiply(10, 2))
    print(shopping_cart.buy("apple"))

if __name__ == "__main__":
    main()