a = 200
b = 10

# this is full form:
if a > b:
    print('a is greater than b')
elif a < b:
    print('a is less than b')
else:
    print('a is equal to b')


# This is short form:
print('a') if a > b else print('b')


# Nested if
if a > 10:
    print('a > 10')
    if a > 100:
        print('and a > 100')
    else:
        print('a < 100')


# Pass statement example
if b > a:
    pass    # for example, we can use it if we don't want to create  logic now
