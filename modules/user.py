class User():
    """A class describing website users"""
    def __init__(self, first_name, last_name, gender, age):
        """initializing class"""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.full_name = self.first_name + ' ' + self.last_name

    def describe_user(self):
        """Brief description of user"""
        print("Name: " + self.full_name.upper())
        print("Gender: " + self.gender.upper())
        print("Age: " + str(self.age))

    def greet_user(self):
        """Greet user"""
        print("\nHello, " + self.first_name)

usr1 = User('hawa', 'abubakar', 'f', 23)
usr1.describe_user()
usr1.greet_user()
