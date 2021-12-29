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


# Object descriptions
car_1 = Car(2021, 'Focus', 'Ford Motorzz', 'gray')
car_2 = Car(2021, '3', 'Mazda Cars', 'red')

# Output for staticmethod
print(Car.car_check('sport'))

# Output for classmethod

print(car_1.getinfosold())
print(car_2.getinfosold())
