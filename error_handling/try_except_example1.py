def div(num1, num2):
    try:
        return num1/num2
    # except:
    #     print('please enter a number')
    #     if you don't specify the error type, you don't know what went wrong
    # except TypeError as err:
    #     print(f'please enter a number, {err}')
    except (TypeError, ZeroDivisionError) as err:
        print(f'please enter a number, {err}')

# print(div('1', 2))
print(div(1, 0))