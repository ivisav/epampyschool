from datetime import date

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
        return (f"Your {self.color} {self.model} sold by '{self.vendor}' in {self.year}")

    @classmethod
    def get_sold_ago(cls, age, model, vendor, color):
        calc_year = date.today().year - age
        return cls(calc_year, model, vendor='NO_NAME', color='White')


# Object descriptions
car_1 = Car(2021, 'Focus', 'Ford Motorzz', 'gray')
car_2 = Car(2011, 'Mazda 3', 'Mazda Cars', 'red')

print(car_1.getinfosold())
print(car_2.getinfosold())

# Output for staticmethod
print(Car.car_check('sport'))

# Output for classmethod
# we don't know the year when the car was produced, lets calculate based on age

car_3 = Car.get_sold_ago(10, 'Mazda 6', 'Mazda Cars', 'red')

# Also, vendor and color will be changed
print(f"It was sold in {car_3.year} ")
print(car_3.getinfosold())
