def my_shiny_function():  # The name of your function
    msg = "It's my new shiny function"  # "body" of your function
    return msg  # The "output" of your function


print('Example 1 result:')
print(my_shiny_function())  # You need to refer to you function to get the result


# You can translate data to functions

def greeting_with_name(name):  # we want to send name to a function
    msg = f"Hi {name}!!"  # we are using the variable
    return msg


print('Example 2 result:')
print(greeting_with_name('Mike'))  # we need to provide value to function.

# You can call your function in cycle to get new result per each object in list
print('Example 3 result:')
names = ['Vasia', 'Lena', 'Nick']
for name in names:
    print(greeting_with_name(name))


# One of the options if we need process multiple conditions inside the function
def my_shiny_func(msg='Hi', *names):
    response = []
    for name in names:
        a = f"{msg} it`s {name}"
        response.append(a)
    return response


print('Example 4 result:')
print(my_shiny_func('Hello', 'Mike', 'Bob', 'Masha'))


def func_args_exmp(name='Bob'):
    msg = f"Hi {name} !"
    return msg


print('Example 5 result:')
print(func_args_exmp())  # You can provide nothing to function - the result will be default value from function


def say_smth(name, msg):
    output = f"{msg} {name}"
    return output


print('Example 6 result:')
print(say_smth(name='Bob', msg='Hey'))  # you can assign value explicitly
