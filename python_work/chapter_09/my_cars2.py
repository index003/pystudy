from car import Car
from electric_car_2 import ElectricCar
from electric_car_2 import ElectricCar as EC

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tasla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

my_tesla = EC('tasla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
