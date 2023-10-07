class Person:
    def __init__(self,pin,aadhar,acc,dob):
        self.pin=pin
        self._aadhar=aadhar
        self.__acc=acc
        self._dob=dob

    def show(self):
        print("Pin is :",self.pin,", Aadhar no is :",self._aadhar," ,Accopunt no is :",self.__acc," ,Date of birth is: ",self._dob)

p=Person(9009,978654233489,2211001500345698,"12/03/2012")
p.show()

print(p.pin)
print(p._Person__acc)
print(p._dob)
print(p._aadhar)