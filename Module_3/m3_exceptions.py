# we want to make simple calculator
# it won't work if input is not an integer

while True:
    try:
        x = int(input("Enter 1st number      "))
    except ValueError:
        print("It's not an integer")
        break

    try:
        y = int(input("Enter 2nd number:        "))
    except ValueError:
        print("It's not an integer")
        break

    z = x + y
    print(f"the result is {z}")
    break
