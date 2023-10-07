import time


# def Add():
#     a=int(input("Enter first name:"))
#     b=int(input("Enter second number:"))
#     sum=a+b
#     print("addition two number",sum)

# class A:
#     def show(self,name,address,salary):
#         self.name=name
#         self.address=address
#         self.salary=salary
#     def work(self):
#         print("name",self.name)
#         print("Address",self.name)
#         print("salary",self.salary)
#
# r=A()
# r.work("rahul","duhai","500000")


import threading

def show(number):
    for _ in range(5):
        print(number)
        time.sleep(3)

v = threading.Thread(target=show("V"))
r = threading.Thread(target=show("r"))

v.start()
r.start()

v.join()
r.join()
print(("all completed"))

