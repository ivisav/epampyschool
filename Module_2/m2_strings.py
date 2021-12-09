expression = "I am Groot"

print('This is full phrase: %s' % expression)  # String with %

print('Only 1st symbol: %(exp_part)s' % {"exp_part": expression[0]})  # string with % and assignment

print(f"Let's cut only name: {expression[5:]}")  # F-string

print('First part w/o name: {}'.format(expression[0:4]))  # string with .format 

print("Character one by one:")
for character in expression:
    print(character)
