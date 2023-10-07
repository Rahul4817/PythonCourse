class A:
    def work(self):
        print("Every car is the 4 wheels")

    def work1(self):
        print("hello world")

    def work2(self):
        print("Rahul is good boy")

    def work3(self):
        print("hello world")


class B(A):
    def work(self):
        print("Every  motercycle is the 2 wheels")

    def work1(self):
        print("how are you rahul")

    def work2(self):
        print("rahul is the bestta ")

    def work3(self):
        print("hello world")

v=A()
v.work()
v.work1()
v.work2()
n=B()
n.work()
n.work1()
n.work2()
