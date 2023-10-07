class Person:
    def __init__(self,name,roll_no):
        self._name=name
        self._roll_no=roll_no

    def get_name(self):# Previous Value
        return self._name

    def set_name(self,name):# here change the actual value
        self._name=name

    def getName(self):# Previous Value
        return self._roll_no

    def setName(self, roll_no): # Here change the value
        self._roll_no=roll_no


p=Person("XYZ","17436")
print("Before change value :",p.get_name())
p.set_name("ABC")
print("After change value :",p.get_name())
print("Before change value :",p.getName())
p.setName("323456455")
print("After change value :",p.getName())
