class Person:
    def __init__(self,pin,aadhar,acc,dob):
        self.pin=pin
        self._aadhar=aadhar
        self.__acc=acc
        self._dob=dob

    def show(self):
        print("Pin is :",self.pin,", Aadhar no is :",self._aadhar," ,Accopunt no is :",self.__acc," ,Date of birth is: ",self._dob)



class Count(Person):

    def display(self, self__acc=None):
        print("Account no is :", self__acc," ,Date of birth is: ", self._dob)

p=Person(0000," ","23456789876578"," ")
c=Count(9009,978654233489,2211001500345698,"12/03/2012")
c.show()
c.display("345678987654")