'''
Terminal game, where the user also inputs lower and upper bounds of the guess. We keep asking the user to guess the number until they get it right.
To run: python guessinggame.py <lower_bound> <upper_bound>
'''
import sys
import random 

def main():
    lower_bound = sys.argv[1]
    upper_bound = sys.argv[2]

    try:
        lower_bound = int(lower_bound)
        upper_bound = int(upper_bound)
    except ValueError:
        print("Please enter valid numberber for the lower and upper bounds of the guess, try again.")
        sys.exit(1)

    number_to_guess = random.randint(lower_bound, upper_bound)
    user_guess = None

    while user_guess != number_to_guess:
        user_guess = input(f"Guess a number between {lower_bound} and {upper_bound}: ")
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Please enter a valid number, try again.")
            continue
    
        if user_guess < number_to_guess:
            print("Too low, try again.")
            lower_bound = user_guess
        elif user_guess > number_to_guess:
            print("Too high, try again.")
            upper_bound = user_guess
        else:
            print("You got it! Congratulations!")
            sys.exit(0)

if __name__ == "__main__":
    main()