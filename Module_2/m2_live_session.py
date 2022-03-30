"""
It's a "board" of actual lecture! Code here has no logic on it's own
All topics are not commented now! Please comment out all of them first to use separately
"""

# Lecture 28.03.2022

a = b = c = 123
print(c, a)

a, b, c = 'A', 'B', 'C'

# Garbege collection
import gc
a, b, *names, c, d = 'A', 'b', 'Igor', 'Mike', 'Alena'
print(type(a))
print(type(names))
print(a)
print(names)
print(c)
print(d)

del d
gc.collect()
print(d)


x = 1
y = 1.1

print(type(x))
print(type(y))

x+=y

print(x)
print(type(x))

print(hex(22))
print(bin(22))
print(oct(22))

print(int('10110', 2))

print(chr(4654))
print(ord('ሮ'))


a = 210
b = 200

if a < b:
    print('a < b')
elif a == b:
    print('a == b')
else:
    print('b < a ')

if a <= b:
    print('a <= b')
    if a == b:
        print('a == b')
    else:
        print('kjfghkjdfhf')
else:
    print('bla bla')

if a > b:
    pass


numbers = [1, 123, 435, 5465]
for i in numbers:
    print(i)

for i in range(1, 10, 2):
    print(i)

x = 2
while True:
    print(x)
    x+=2
    if x > 200:
        break

number = 0
while number < 5:
    print(number)
    number+=1
else:
    print(f"number reached {number}")

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

print(10 & 4)
print(10 | 4)
print(10 ^ 9)

print(int('0011', 2))

st_in_cls = ['Mike', 'Bob', 'Ivan']
if 'Ivan' in st_in_cls:
    print('Ivan is here')
if 'Masha' not in st_in_cls:
    print('Masha is not here')

a = 1.0
print(type(a))
if type(a) is float:
    print('a is float')
else:
    print('a is not float')

wish_food = 'fish'
money = 0
            #             True
            #                                 False
            # True                    False           False
if (wish_food == 'fish' or wish_food == 'salad') and money >= 15:
    print('Here is your food')
else:
    print('no food for you today')

expression = "I am Groot"
print(expression[::-1])
for chr in expression:
    print(chr)


name = 'Igor'
sr_na = 'GJHlkgdj'
print('Hi, %(name)s %(sr_na)s' % {"name": name, "sr_na": sr_na})

print('Hi, {}'.format(name))
print('Hi, {} {} {}'.format(name, sr_na, 'bla bla'))

print(f'Hi {sr_na} {name}')

print(name + ' ' + sr_na)

https://docs.python.org/3/library/decimal.html

from decimal import *
getcontext().prec = 2
print(1 / 7)
print(Decimal(1) / Decimal(7))
print(Decimal(1.1) + Decimal(2.2))

import random
print(random.randrange(0, 1000))