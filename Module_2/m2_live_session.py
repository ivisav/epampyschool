"""
It's a "board" of actual lecture! Code here has no logic on it's own
All topics are not commented now! Please comment out all of them first to use separately
"""

# === Assignment ===
a = 123
print(a)

a = b = c = 0
print(b)

a, b, c = 'letter A', 'letter B', 'letter C'
print(b)

now_time, ip, *payload = '18:44', '8.8.8.8', 'asd', 'gfdf', 'gfgkjhf'
print(payload)
print(now_time)

# === Data types and type conversion==

print(type(ip))
print(type(payload))
a = 1
a = 1234
b = 1.1
print(type(a))
print(type(b))
a = a + b
print(type(a))
print(int('10101', 2))
print(bin(21))
print(ord('ᑱ'))

# === Comparison  ===
a = 123
b = 321

if a > b:
    print('a > b')
elif a == b:
    print('a = b')
else:
    print('b > a')

print('a < b') if a < b else print('asfg')

a = 123
b = 321
if a < b:
    if a + b > 400:
        print(a + b)
    else:
        print('asdf')
else:
    print('fdsf')

a = 123
b = 321

if a > b:
    pass

# === Loops ===
names = ['Mike', 'Anton', 'Masha']
for name in names:
    print(f'Hi {name}')

for i in range(3):
    print(i)

i = 0
while True:
    print(i)
    i += 1
    if i > 100:
        break

i = 0
while i < 5:
    print(i)
    i += 1
else:
    print('this is it')

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

# === Membership Operators ===
names = ['Alena', 'Bob', 'Igor']
if 'Igor' in names:
    print('Igor is here')
if 'Mike' not in names:
    print('Mike is not here')

# === Identity Operators ===

a = 1
print(type(a))
if type(a) is int:
    print('it is string')

# Priority of operators example
# !! You need to add () to make it work as expected

wish_food = 'salad'
money = 0

if wish_food == 'salad' or wish_food == 'steak' and money >= 15:
    print('Here is your food')
else:
    print('sorry, no food for you today')

# === Strings ===

a = 'I am Groot'
print(a[0])
print(a[5:6])
print(a[::-1])

for chr in a:
    print(chr)

name = 'Igor'
fname = 'Bob'
# print('hi %s' %name)

greetings = 'Hi {my_n},  this is {f_n}'.format(f_n=fname, my_n=name)
print(greetings)

print(f'Hi {name}, this is {fname}')

# === Numbers ===

print(0.1 + 0.1 + 0.1 - 0.3)

print(1.1 + 2.2)

from decimal import *

getcontext().prec = 1
print(Decimal(1.1) + Decimal(2.2))
a = 1.1 + 2.2
print(Decimal(a))

# import random
# print(random.randrange(0, 100))
