# LEGB rule example

# Local (or function) scope
def legb():
    x = 'legb'
    print(x)
legb()
# print(x)  << it won't work coz out of scope


# Enclosing (or nonlocal) scope
def tests_out():
    x = 'outer'

    def test_inn():
        y = 'inner'
        print(f'this is {y} and this is {x}')
        print(x)

    test_inn()
tests_out()
# we will see both x and y results. Inner function as it is nested function


# Global (or module) scope
global_var = 'I am global variable'

def example_2():
    print(global_var)

    def example_2_inn():
        print(f"Variable called in inner function: {global_var}")

    example_2_inn()
example_2()
# We will get result from both calls


# Built-in Scope
from math import pi

def example():
    def example_inner():
        print(pi)

    print(pi)
    example_inner()
example()
print(pi)
# we will see 3 outputs of pi number from different scopes
