#Python polymorphism
class Animal:
    def speak(self):
        return "Generic animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())

print("*****************************************************************************************")

import pandas as pd
list = [1,2,3,4,4,5]
res = pd.Series(list)
print(res)

print("*****************************************************************************************")
