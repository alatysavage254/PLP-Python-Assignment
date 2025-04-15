#Assignment 1: Design Your Own Class!
# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city
        self.__real_identity = "Unknown"  # Encapsulated attribute

    def set_identity(self, identity):
        self.__real_identity = identity

    def get_identity(self):
        return self.__real_identity

    def introduce(self):
        print(f"I am {self.name}, protector of {self.city} with the power of {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power} to save the day!")

# Derived class with polymorphism
class TechHero(Superhero):
    def __init__(self, name, city, gadget):
        super().__init__(name, "Advanced Technology", city)
        self.gadget = gadget

    # Overriding use_power
    def use_power(self):
        print(f"{self.name} hacks into enemy systems using the {self.gadget}!")

# Creating instances
hero1 = Superhero("Captain Blaze", "Fire Control", "Metro City")
hero1.set_identity("Jordan Blaze")

hero2 = TechHero("CyberKnight", "Neo Tokyo", "Quantum Suit")

# Using methods
hero1.introduce()
print(f"Real Identity: {hero1.get_identity()}")
hero1.use_power()

print("\n---\n")

hero2.introduce()
hero2.use_power()


#Activity 2: Polymorphism Challenge! 
class Vehicle:
    def move(self):
        print("This vehicle moves in some way.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water 🚢")

# Polymorphism in action
def vehicle_action(vehicle):
    vehicle.move()

# Creating objects
my_car = Car()
my_plane = Plane()
my_boat = Boat()

# Test all vehicle movements
vehicle_action(my_car)
vehicle_action(my_plane)
vehicle_action(my_boat)
