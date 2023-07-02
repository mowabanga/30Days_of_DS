class Restaurant():
    """A simple restaurant class."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initializing restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """What type of restaurant it is"""
        print(self.restaurant_name.title() + " is an Ethiopian restaurant.")
        print("We offer " + self.cuisine_type.title() + " cuisine.")

    def open_restaurant(self):
        """Open or closed?"""
        print(self.restaurant_name.title() + " is now open.")

restaurant = Restaurant('habeshi', 'ethiopian')

restaurant.describe_restaurant()
restaurant.open_restaurant()
