def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator) # the same memory address
            print(next(iterator))
        except StopIteration:
            break

# that's how the for loop works
special_for([1, 2, 3])

# defining a generator class to see how generators work under the hood
class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self): # we want to be able to iterate over this class
        return self
    
    def __next__(self): # for loop will call this method
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration

gen = MyGen(0, 100)
for i in gen:
    print(i)