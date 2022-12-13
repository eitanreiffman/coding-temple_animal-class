# Exercise 2:
# Write a Python class for an Animal that has a name and energy attributes.
# The animal class should also have methods for eat, sleep, and play that will
# take in an integer and increase/decrease the energy of the animal with a formatted print statement

# Example 1
# buddy = Animal('Buddy', 10)
# buddy.play(5) -> "Buddy is playing for 5 minutes. His energy is now 5"
# buddy.sleep(10) -> "Buddy is sleeping for 10 minutes. His energy is now 15"

class Animal:
    def __init__(self, name, energy=10):
        self.name = name
        self.energy = energy

    def eat(self, food_amount):
        energy_increase = food_amount * 3
        self.energy += energy_increase
        print(f"\nAfter eating {food_amount} portions of food, the {self.name}'s energy has increased by {energy_increase}\n")
        print(f"Now the {self.name} has an energy level of {self.energy}\n")


    def sleep(self, hour_amount):
        energy_increase = hour_amount
        self.energy += hour_amount
        print(f"\nAfter sleeping for {hour_amount} hours, the {self.name}'s energy has increased by {energy_increase}\n")
        print(f"Now the {self.name} has an energy level of {self.energy}\n")

    def play(self, minute_length):
        energy_decrease = minute_length // 20
        self.energy -= energy_decrease
        print(f"\nAfter playing for {minute_length} minutes, the {self.name}'s energy has decreased by {energy_decrease}\n")
        print(f"Now the {self.name} has an energy level of {self.energy}\n")        

animal1 = Animal('cheetah')
print(animal1.__dict__)

animal2 = Animal('lion')
print(animal2.__dict__)

animal3 = Animal('gorilla')
print(animal3.__dict__)

animal1.eat(3)

animal2.sleep(8)

animal3.play(90)
