# #
# # #Duck type ploymorphism
# class Cat:
#     def sound(self):
#         return "Meow"
#
# class Dog:
#     def sound(self):
#         return "Woof"
#
# for animal in [Cat(), Dog()]:
#     print(animal.sound())  # Outputs "Meow" and "Woof" based on the object's behavior.
#
#
# # # Polymorphism with inheritance
#
# class Animal:
#     def speak(self):
#         pass
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow"
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof"
#
# for animal in [Cat(), Dog()]:
#     print(animal.speak())  # Outputs "Meow" and "Woof" based on the subclass implementation.
#
# #
# # #Method overriding
#
# class Calculator:
#     def add(self, x, y=0):
#         return x + y
#
# calc = Calculator()
# print(calc.add(5))       # Outputs 5
# print(calc.add(2, 3))    # Outputs 5
#
#
# # #Operator overloading
# #
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# result = v1 + v2

#
# #Abstract Base Classes
#
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
#
#
# class person:
#     def __init__(self,name,age,address):
#         self.name=name
#         self._age=age
#         self.__address=address
#
# v=person("rahul",23,30000)
# print(v.name)
# print(v._age)
# print(v._person__salary)


class person:
    def __init__(self,name,age,address):
        self.name=name
        self._age=age
        self.__address=address

    def work(self):
        print("name",self.name)
        print("age",self._age)
        print("address",self.__address)

p1 = person("rahul",31,300000)
p1.work()
