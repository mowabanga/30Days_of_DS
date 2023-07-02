class Car():
    """Simple attempt to represting car"""

    def __init__(self, make, model, year):
        """inistantizing class"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def desc_name(self):
        """descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """current mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """updating miles on odometer"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        """Automatically increment odometer"""
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represents aspects of a car specific to an electric car"""
    def __init__(self, make, model, year):
        """Initialize attributes of parent class"""
        super().__init__(make, model, year)
        self.battery_size = 70

    def desc_batt(self):
        """describe battery size"""
        print("This car has a " + str(self.battery_size) + "-kWh battery")

my_tesla = ElectricCar('tesla', 'model x', 2018)
print(my_tesla.desc_name())
my_tesla.read_odometer()
my_tesla.update_odometer(245)
my_tesla.read_odometer()
my_tesla.increment_odometer(55)
my_tesla.read_odometer()
my_tesla.desc_batt()
