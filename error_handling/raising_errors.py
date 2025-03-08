while True:
    try:
        age = int(input('what is your age?' ))
        10/age
        raise Exception('hey cut it out')
    # except ValueError:
    #     print('please enter a number')
    #     continue
    except ZeroDivisionError:
        print('please enter a number greater than 0')
        break
    else:
        print('thank you')
        break
    finally: # runs regardless of the outcome
        print('ok, I am finally done')