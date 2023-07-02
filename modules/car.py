class Car():
    """A class describing cars"""

    def __init__(self, make, model, year):
        """Inititalize attributes to describe car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing car mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer to the given value.
        Reject the change if it attempts to roll over the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        """Add given amount to odometer reading"""
        self.odometer_reading += miles

new_car = Car('toyota', 'harrier', 2012)
print(new_car.get_descriptive_name())
new_car.update_odometer(459)
new_car.read_odometer()
new_car.increment_odometer(30)
new_car.read_odometer()
