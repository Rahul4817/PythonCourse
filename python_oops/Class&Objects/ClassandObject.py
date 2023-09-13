class Car:

    def __init__(self,car_name,car_model,car_brand,car_price):
        self.car_name=car_name
        self.car_model = car_model
        self.car_brand = car_brand
        self.car_price = car_price

    def show(self):
        print("Car Name:",self.car_name)
        print("Car Model:", self.car_model)
        print("Car Brand:", self.car_brand)
        print("Car Price:", self.car_price)

car=Car("toyota",2023,"supra",3000000000)
print(car.show())
