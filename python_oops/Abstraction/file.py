from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def get_details(self):
        pass


class Student(Person):
    def __init__(self,name,roll_no):
        super().__init__(name)
        self._roll_no=roll_no

    def get_details(self):
        return f"Name is: {self.name}, Roll number: {self._roll_no}"

class Facalty(Person):
    def __init__(self,name,factly_id):
        super().__init__(name)
        self._factly_id=factly_id

    def get_details(self):
        return f"Name: {self.name}, Factly_id is {self._factly_id}"


student=Student("Naurangi","ER231")
facalty=Facalty("Naurangi lal","FT104")
print(student.get_details())
print(facalty.get_details())
