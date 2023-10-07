
# Polymorphism with runtime

class Method:
    def __init__(self,name):
        self.name=name

    def get_details(self):
        return f" Name : {self.name}"


class Driver(Method):

    def __init__(self,name,roll_no):
        super().__init__(name)
        self._roll_no=roll_no

    def get_details(self):
        return f"New name :{self.name},and roll_no is {self._roll_no}"


method=Method("Rahul")

driver=Driver("Rahul kumar","041")

print(method.get_details())
print(driver.get_details())



# Polymorphism with function

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

# Polymorphic function
def animal_sound(animal):
    return animal.speak()
# Create instances of different animals
dog = Dog()
cat = Cat()
duck = Duck()


print(animal_sound(dog))
print(animal_sound(cat))
print(animal_sound(duck))
