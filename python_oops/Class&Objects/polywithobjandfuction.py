class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Polymorphic function
def calculate_area(shape):
    return shape.area()

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(calculate_area(circle))
print(calculate_area(rectangle))




# Function parameters

class Car:
    def engine_start(self):
        pass

class ElectricCar(Car):
    def engine_start(self):
        return "Electric engine started"

class LpgCar(Car):
    def engine_start(self):
        return "LPG engine started"

# Polymorphic function
def start_car_engine(car):
    return car.start_engine()

electric_car = ElectricCar()
gasoline_car = LpgCar()

print(start_car_engine(electric_car))
print(start_car_engine(gasoline_car))
