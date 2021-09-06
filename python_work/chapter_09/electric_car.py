class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back odometer!")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back odometer!")

    def fill_gas_tank(self):
        print("This car have a gas tank!")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        # 继承父类属性
        super().__init__(make, model, year)
        # 自己的属性
        self.battery_size = 75

    # 子类自己的方法
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    # 子类重写父类方法
    def fill_gas_tank(self):
        print("ElectricCar doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
