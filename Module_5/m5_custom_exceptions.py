# We want to make our calc to calculate only numbers where x > 0

class LessThanZero(Exception):
    def __init__(self, msg, context):
        self.message = msg
        self.context = context
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.context}"


while True:
    try:
        x = int(input("Enter 1st number      "))
    except ValueError:
        print("It's not an integer")
        break
    try:
        if x < 0:
            raise LessThanZero('Value less than 0, your value is', x)
    except Exception as e:
        print(e)
        break
    try:
        y = int(input("Enter 2nd number:        "))
    except ValueError:
        print("It's not an integer")
        break

    z = x + y
    print(f"the result is {z}")
    break
