def ask_age():
    try:
        age = int(input('what is your age?' ))
        print(f'you are {age} years old')
    except:
        print('please enter a number')
        ask_age()
    return age

# ask_age()

while True:
    try:
        age = int(input('what is your age?' ))
        if age == 0:
            print('age cannot be 0')
            continue
        print(f'you are {age} years old')
    except ValueError:
        print('please enter a number')
    else:
        print('thank you')
        break
