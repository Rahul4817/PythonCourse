from abc import ABC,abstractmethod
class A(ABC):
    def show(self):
        print("every car has the 4 wheels")

    @abstractmethod
    def milege(self):
            pass
class tvs(ABC):
    def milege(self):
        print("milege is the 100km/h")

class honda(ABC):
    def milege(self):
        print("milege is the 80km/h")

class ct100(ABC):
    def milege(self):
        print("milege is the 100km/h")

v=tvs()
v.milege()

t=honda()
t.milege()

r=ct100()
r.milege()