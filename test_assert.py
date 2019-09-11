# -*- coding:utf-8 -*-

# usage of assert
aogo_input = input('please certify your age')
aogo_str = int(aogo_input)
assert 20 < aogo_str <= 30
print('the age is betwenen 20 ~30')

# return the discount price
def apply_discount(price, discount):
    update_price = price * (1 - discount)
    assert 0 < update_price < price, "the update_price is between 0 ～ %s" % price
    return update_price


print (apply_discount(100, 0.8))
print (apply_discount(100, 1.1))

