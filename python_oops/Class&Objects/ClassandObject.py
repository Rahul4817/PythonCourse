class Car:
    def __init__(self, car_name, car_model, car_brand, car_price):
        self.car_name = car_name
        self.car_model = car_model
        self.car_brand = car_brand
        self.car_price = car_price

    def show(self):
        print("Car Name:", self.car_name)
        print("Car Model:", self.car_model)
        print("Car Brand:", self.car_brand)
        print("Car Price:", self.car_price)


class Student:
    def __init__(self, name, address, salary):
        self.name = name
        self.address = address
        self.salary = salary

    def display(self):
        print("student name", self.name)
        print("student address:", self.address)
        print("Salary is ", self.salary)




car = Car("Toyota", 2023, "Supra", 3000000000)
car.show()

s = Student("ABC","Unknown place:","😒😒😒😒😒   ....")
s.display()
