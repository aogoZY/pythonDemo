# -*- coding:utf-8 -*-

# list usage
# create list
test_list = ['aogo', 'amao', 'azhu']

# get list value
print (test_list[0])    # aogo
print (test_list[-1])   # azhu

# get the length of list
print (len(test_list))  # 3

# append element
test_list.append('aniu')
print (test_list)   # ['aogo', 'amao', 'azhu', 'aniu']

# insert the element
test_list.insert(0,'aogo2')
print (test_list)   # ['aogo2', 'aogo', 'amao', 'azhu', 'aniu']

# delete the end element
print (test_list.pop())     # aniu
print (test_list)           # ['aogo2', 'aogo', 'amao', 'azhu']
print (test_list.pop(0))    # aogo2
print (test_list)           # ['aogo', 'amao', 'azhu']

# replace the element
test_list[0] = 'aogo3'
print (test_list)       # ['aogo3', 'amao', 'azhu']

# delete the element based on index
del test_list[1]
print (test_list)       # ['aogo3', 'azhu']
del test_list[0:2]
print (test_list)       # []

# list() function create list
test_range = range(1,5)
list_range = list(test_range)
print (list_range)    # [1, 2, 3, 4]

# remove the element
list_range.remove(2)
print (list_range)      # [1, 3, 4]

# count the element time
list_str = ['aogo', 23, 'azhu', 45, 3, 'aogo']
print (list_str.count('aogo'))      # 2

# find the index
print (list_str.index('azhu'))  # 2
