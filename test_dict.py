# -*- coding:utf-8 -*-
#  the usage of dict

# create dict using {}
test_dict = {'one': 1, 'two': 2, 'three': 3}
print (type(test_dict))     # <type 'dict'>

# create dict using formkeys()
subjec = {'english', 'math', 'chinese'}
score = dict.fromkeys(subjec)
print (score)       # {'chinese': None, 'math': None, 'english': None}
print (type(score))  # <type 'dict'>

# cerate dict using dict() & zip()
keys = ['one', 'two', 'three']
values = [1, 2, 3]
aogo_dict = dict(zip(keys, values))
print (aogo_dict)       # {'three': 3, 'two': 2, 'one': 1}
print (type(aogo_dict))     # <type 'dict'>

# get the element
value_one = aogo_dict['one']
print (value_one)       # 1

values_two = aogo_dict.get('two')
print (values_two)      # 2

# when the key is not defined, set the default value not to raise the err
values_four = aogo_dict.get('four','the value is not defined')
print (values_four)     # the value is not defined

# delete the dict
# del aogo_dict
# print (aogo_dict)   # NameError: name 'aogo_dict' is not defined

# add the element
a_dict = {'name': 'aogo'}
print (a_dict)      # {'name': 'aogo'}
a_dict['age'] = 18
print (a_dict)      # {'age': 18, 'name': 'aogo'}

# change the element
a_dict['age'] = 19
print (a_dict)      # {'age': 19, 'name': 'aogo'}

# del the element
del a_dict['age']
print (a_dict)      # {'name': 'aogo'}

# whether the key-value is existed （use th e key）
print ('name' in a_dict)        # True
print ('grade' in a_dict)       # False
print ('age' not in a_dict)     # True

# show the  kyes\values\items
b_dict = {'name': 'ali', 'age': 12, 'color': 'red'}
print (b_dict.keys())       # ['color', 'age', 'name']
print (b_dict.values())         # ['red', 12, 'ali']
print (b_dict.items())      # [('color', 'red'), ('age', 12), ('name', 'ali')]

for k in b_dict.keys():
    print(k)
for v in b_dict.values():
    print (v)
for k,v in b_dict.items():
    print (k, v)
# color
# age
# name

# red
# 12
# ali

# ('color', 'red')
# ('age', 12)
# ('name', 'ali')

# update the k,v when key existed,change the value,when key not existed,new a k,v
c_dict = {'one': 1, 'two': 2, 'three':3}
c_dict.update({'one': 0, 'four': 4})
print (c_dict)      # {'four': 4, 'three': 3, 'two': 2, 'one': 0}

# delete the key of the value
print (c_dict.pop('one'))
print (c_dict)      # {'four': 4, 'three': 3, 'two': 2}

# random pop k,v
# pop up the last key-value pair,but the order in the dict is agnostic
print (c_dict.popitem())    # ('four', 4)
print (c_dict)      # {'three': 3, 'two': 2}

# Format a string using a dictionary
temp = "the book name is: %(name)s, the price is : %(price)d, the publish is : %(publish)s"
book = {'name': 'python study', 'price': 99, 'publish': 'chinese publish'}
print (temp % book)     # the book name is: python study, the price is : 99, the publish is : chinese publish
book2 = {'name': 'java coding', 'price': 88, 'publish': 'america publish'}
print (temp % book2)    # the book name is: java coding, the price is : 88, the publish is : america publish

