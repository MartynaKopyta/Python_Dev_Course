from time import time

def performance(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Time elapsed: {end_time - start_time}")
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(100000):
        i*5

@performance
def long_time2():
    print('2')
    for i in list(range(100000)):
        i*5 

long_time() # faster
long_time2()