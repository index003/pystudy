
class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog's is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog's is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()
