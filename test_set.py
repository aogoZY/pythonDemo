# -*- coding:utf-8 -*-
# usage of set

# create set afford a list
aogo_set = set(['c', 1, 2, 'c', 1])
# no duplicate value & no order
print (aogo_set)         # set([1, 'c', 2])
print (type(aogo_set))  # <type 'set'>

# find the element
for ele in aogo_set:
    print (ele)
    # 1
    # c
    # 2

# remove the element
aogo_set.remove('c')
print (aogo_set)        # set([1, 2])

# add the element
aogo_set.add('d')
print (aogo_set)        # set([1, 2, 'd'])
