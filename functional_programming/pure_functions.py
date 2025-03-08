# What is functional programming? Code that is:
# Clear + understandable
# Easy to extend
# Easy to maintain
# Memory efficient
# DRY (no repetitions)

# main concept - pure functions
# given the same input, the same output
# does not produce side effects (for ex. no printing, no touching anything in the outside world)
# separating data and functions
# keeping code clean and avoiding bugs with these when possible

def multiply_by2(li):  # passes both tests
    new_list = []  # if list was outside also side effects, interacting with a list outside the function
    for item in li:
        new_list.append(item * 2)
    return new_list  # if we printed here, there would be side effects


print(multiply_by2([1, 2, 4]))
