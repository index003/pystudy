from electric_car_1 import Car, ElectricCar
import electric_car_1

# 导入多个类
my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tasla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# 导入整个模块
my_beetle = electric_car_1.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = electric_car_1.ElectricCar('tasla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
