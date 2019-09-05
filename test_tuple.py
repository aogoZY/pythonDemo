# -*- coding:utf-8 -*-

# tuple unchangeable

# tuple usage
# creating a tuple
aogo_tuple = ('goog', 'study', 'hard', 'work')
print (type(aogo_tuple))       # <type 'tuple'>

test_range = range(1, 5)
print (test_range)      # [1, 2, 3, 4]
print (type(test_range))    # <type 'list'>
test_tuple = tuple(test_range)
print (test_tuple)      # (1, 2, 3, 4)

# when there is only one element
simple_tuple = (1,)
print (type(simple_tuple))      # <type 'tuple'>
simple_tuple2 = (1)
print (type(simple_tuple2))     # <type 'int'>

# find the element
# find the element index from 0~1
print (aogo_tuple[:2])      # ('goog', 'study')

