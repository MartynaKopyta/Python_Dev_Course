# Generators allow you to generate a swquence of values over time

# Example
range(100) # This is a generator

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100) # this is takig up memory
print(my_list)
# vs range doesn't create a list in memory, it generates the numbers on the fly
# especially for large numbers, this is more efficient - we generate items one by one

# iterable - any object in python that can be looped over
# generator - a special type of iterable that does not store values in memory

def generator_function(num):
    for i  in range(num):
        yield i 
        
# yield pauses the function and comes back to it when called again
# for item in generator_function():
#     print(item)

g = generator_function(100) # this is a generator object
print(g)
print(next(g)) # the function was paused at yeild and it did the next step only when we asked
print(next(g))

# we still need to mind the range (num) in the generator function


