#
# # Through Method Overriding
#
# class Animal:
#     def speak(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
#
# dog = Dog()
# cat = Cat()
#
# print(dog.speak())  # Outputs: Woof!
# print(cat.speak())  # Outputs: Meow!
#
#
# #Through polymorphic behavier
# def make_animal_speak(animal):
#     return animal.speak()
#
# dog = Dog()
# cat = Cat()
#
# print(make_animal_speak(dog))
# print(make_animal_speak(cat))

#
# class A():
#     def work(self):
#         print("New Delhi is the capital of India.")
#
#     def work1(self):
#         print("Hindi is the most widely spoken language of India.")
#
#     def work2(self):
#         print("India is a developing country.")
#
#
# class B():
#     def work(self):
#         print("Washington, D.C. is the capital of USA.")
#
#     def work1(self):
#         print("English is the primary language of USA.")
#
#     def work2(self):
#         print("USA is a developed country.")
# # Through Fuction
# def turn(obj):
#     obj.work()
#     obj.work1()
#     obj.work2()
#
# a=A()
# turn(a)
# b=B()
# turn(b)

#Through Classobject method
# v = A()
# v.work()
# v.work1()
# v.work2()
#
# t = B()
# t.work()
# t.work1()
# t.work2()

#Through Duck Typing
# v=A()
# T=B()
# for x in (v,T):# => Duck typing method in python
#     x.work()
#     x.work1()
#     x.work2()



## inheritance method
# class A:
#     def work(self):
#         print("There are many types of birds.")
#
#     def work1(self):
#         print("Most of the birds can fly but some cannot.")
#
#
# class B(A):
#     def work1(self):
#         print("Sparrows can fly.")
#
#
# class C(A):
#     def work(self):
#         print("Ostriches cannot fly.")
#
#
# v = A()
# t = B()
# r = C()
#
# v.work()
# v.work1()
# t.work()
# t.work1()
# r.work()
# r.work1()

#methodOverloading

class MyClass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("Sum of these is :",a+b+c)
        elif a!=None and b!=None:
            print("Sum of these is :",a+b)
        else:
            print("Arguments are more than given parameters!")

S=MyClass()
S.sum(10,20,10)
S.sum(20,30)