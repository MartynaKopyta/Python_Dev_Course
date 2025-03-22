# 1 - collections
from collections import Counter, defaultdict, OrderedDict

# Counter
li = [1, 2, 3, 4, 5, 6, 7, 7]
counted = Counter(li)
# print(counted) # Counter({7: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
for key, count in counted.items():
    print(f'{key}: {count}') # 7: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1

sentence = "blah blah blah thinking about python"
print(Counter(sentence)) # Counter({' ': 5, 'h': 4, 'b': 4, 'a': 3, 'l': 3, 't': 3, 'n': 3, 'i': 3, 'g': 2, 'o': 2, 'k': 1, 'u': 1, 'p': 1, 'y': 1})

# defaultdict
dictionary = {'a': 1, 'b': 2}
print(dictionary['a']) # 1
# print(dictionary['c']) # KeyError: 'c'

# we can set a default value for the dictionary, it has to be a callable so we can use lambda
default_dict = defaultdict(lambda: 0, {'a': 1, 'b': 2})
print(default_dict['d']) # 1

# OrderedDict - deprecated in Python 3.7, it is now a built-in feature of the dict class
d1= OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2= OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d1 == d2) # False


# 2 - datetime
import datetime

print(datetime.time()) # 00:00:00
print(datetime.time(5, 45, 2)) # 05:45:02
print(datetime.date.today()) # date in format yyyy-mm-dd
print(datetime.datetime.now()) # date and time in format yyyy-mm-dd hh:mm:ss.123456


# 3 - time
# we can use time to measure for example how long a piece of code takes to run


# 4 - array
# in python lists are more flexible than arrays, we can keep adding elements to them
# arrays are more efficient in terms of memory usage and performance
# arrays sets how much memeory it takes up in advance, what datatype is going to be stored

from array import array

arr = array('i', [1, 2, 3]) # i stands for integer
print(arr[0]) # 1