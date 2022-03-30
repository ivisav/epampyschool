expression = "I am Groot"

print('This is full phrase: %s' % expression)  # String with %

print('Only 1st symbol: %(exp_part)s' % {"exp_part": expression[0]})  # string with % and assignment

print(f"Let's cut only name: {expression[5:]}")  # F-string

print('First part w/o name: {}'.format(expression[0:4]))  # string with .format

print('First is {2}, second is {0}, third is {1}. '.format('first', 'second', 'third'))
# We can choose particular argument. Similar to index in List datatype.

print('Hi ' + name + ', this is ' + friend_name) #We can use symbol "+" for concatenate string and variable.

print("Symbol one by one:")
for symbol in expression:
    print(symbol)
