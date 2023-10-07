class Student:
    def __init__(self,name,roll,per):
        self.name=name
        self.roll=roll
        self.per=per
obj=Student("Rahul","34","34.6")
print(obj.name,obj.roll,obj.per)


class A:
    def work(self):
        print("Rahul to going to school")

    def language(self):
        print("once upon a time")

    def show(self):
        print("Hello world")


class B:
    def work(self):
        print("Rahul from the sambhal")

    def language(self):
        print("python is the high leval programing language")

    def show(self):
        print("overloding is the same method and differnt parameter")


V = A()
T = B()
# Duck type polymorphism

for x in (V,T):
    x.work()
    x.language()
    x.show()