"""
It's a "board" of actual lecture! Code here has no logic on it's own
All topics are not commented now! Please comment out all of them first to use separately
"""


# === How to get all  variable that are identical (based on one object)===
list_1 = list_2 = ['abc', 'bca']
list_3 = list_1
list_4 = ['abc', 'bca']
list_5 = list_4

print(list_1 is list_2)
print(list_1 is list_4)

def check_eq(item):
    return [name for name, val in globals().items() if val is item]

print(check_eq(list_4))

# === Function with *args ===

def my_shiny_func(msg='Hi', *names):
    response = []
    for name in names:
        a = f"{msg} it`s {name}"
        response.append(a)
    return response


print(my_shiny_func('Hello', 'Mike', 'Bob', 'Masha'))

import sys

print('\n'.join(sys.path))

print(dir(sys))

# ===   Inner and outer functions   ===

def exam():
    print('I am outer')
    def exam_1():
        print('I am inner')
    exam_1()
print(exam())

def func_arg(name, *scores):
    print(f'Name: {name}')
    print('Score:')
    for score in scores:
        print(score)

func_arg('Mike', 90, 100, 95)

# ===   **kwargs example    ===

def print_dog_info(owner, **dog):
    print(f'Owner: {owner}')
    for breed, name in dog.items():
        print(f"{breed}: {name}")


print_dog_info('Igor', sheepherd='Grace', aussie='Meonia')
import math

f = 213

# ===   LEGB logic (check m4_legb_rule.py for more details) ===
def exmp():
    x = 123
    print(f)
    print(math.pi)
    def exmp_1():
        y = 3212
        z = f+y
        print(z)
        print(math.pi)
    exmp_1()

print(exmp())
print(f)


print(math.pi)

# ===   First class functions   ===

def calc_exp(base, exp):
    return base ** exp

def calc(method, exponents):
    result = []
    for item in exponents:
        result.append(method(2,item))
    return result

final_result = calc(calc_exp, [2,5,6,7,10,12])
print(final_result)

# === Decorators ===
def decorator_func(org_func):
    def sep_tulp(tupls):
        return [org_func(elem[0], elem[1]) for elem in tupls]
    return sep_tulp


@decorator_func
def speech(name, phr):
    print(f"{name} : {phr}")

speech([('Igor', 'bla bla bla'), ('Mike', 'bla bla bla!!')])


# ===   Classes   ===
# it's a fixed version, you can find the same in separate example

class Car:
    def __init__(self, year, model, vendor, color='black'):
        self.year = year
        self.vendor = vendor
        self.color = color
        self.model = model

    @staticmethod
    def car_check(car_type):
        if car_type == 'sport':
            return 'You can go to track'
        else:
            return 'Only calm ride for you'

    def getinfosold(self):
        return (f"your car sold by '{self.vendor}' in {self.year}")

    @classmethod
    def get_sold_info(cls, year, vendor):
        return cls(year, vendor)

car_1 = Car(2021, 'Focus', 'Ford Motorzz', 'gray')
car_2 = Car(2021, '3', 'Mazda Cars', 'red')

print(Car.car_check('sport'))

print(car_1.getinfosold())
print(car_2.getinfosold())
