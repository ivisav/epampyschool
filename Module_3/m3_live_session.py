"""
It's a "board" of actual lecture! Code here has no logic on it's own
All topics are not commented now! Please comment out all of them first to use separately
"""

# ===    Lists explanation   ===
fruits = ['apple', 'orange', 'plum']
print(type(fruits))

fruits[0] = 'kiwi'
print(fruits)

fruits.append('apple')
print(fruits)

fruits.insert(2, 'lemon')
print(fruits)

print(len(fruits))

a = [['a', 'b'], ['c', 'd'], 'apple', {}]
print(all(a))
print(any(a))

print(list('hello world'))

fruits = ['apple', 'orange', 'plum']

len(fruits)

fruits.append('kiwi')

print(fruits)

# ===   is and == explanation on an example     ===
# For more clear code please refer to m3_lists_example.py

fruits_1 = fruits_3 = ['orange', 'apple', 'plum']
fruits_2 = ['plum', 'orange', 'apple']

print(fruits_1 == fruits_2)
print(fruits_1 == fruits_3)

fruits_1.sort()
fruits_2.sort()

print(fruits_1 == fruits_2)
print(fruits_1 is fruits_2)

print(fruits_3 == fruits_2)
print(fruits_3 is fruits_2)
print(fruits_3)

print(id(fruits_1))
print(id(fruits_2))
print(id(fruits_3))
print(fruits_3 is fruits_1)

fruits_1.append('kiwi')
print(fruits_3)

fruits_4 = fruits_3
print(fruits_4 is fruits_1)

del (fruits_1)
print(fruits_4)

fruits_5 = fruits_4.copy()
print(id(fruits_5))
print(id(fruits_4))
fruits_4.append('kiwi')
print(fruits_4)
print(fruits_5)

# ===   SETS    ===

set_fruits_1 = {'apple', 'orange', 'plum', 'kiwi'}
set_fruits_2 = {'apple', 'orange1', 'plum', 'kiwi1'}

print(set_fruits_1.intersection(set_fruits_2))

cat = {'breed': 'no_name', 'legs': 4, 'age': 'old', 'color': 'black'}
print(cat['legs'])
print(cat.values())

cat['color'] = 'red'
print(cat)

print(tuple('hello world'))


#   ===     FUNCTIONS   ===

def my_shiny_func(msg='Hi', *names):
    for name in names:
        a = f"{msg} it`s {name}"
        return a


print(my_shiny_func('Hello', 'Mike', 'Bob', 'Masha'))

# ===   Exceptions    ===

while True:
    try:
        x = int(input('Provide 1st number:          '))
        y = int(input('Provide 2nd number:          '))
        div_result = x / y
        print(div_result)
        break
    except ZeroDivisionError:
        print('Please provide smth else')
    except ValueError:
        print('Only int here')
