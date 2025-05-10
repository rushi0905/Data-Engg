# class base1:
#     def read(self):
#         self.num1 = int(input("Enter the first num : "))
#         self.num2 = int(input("Enter the second num : "))
#         self.num3 = int(input("Enter the third num : "))
#
# class derive1(base1):
#     def operations(self):
#         add = self.num1 + self.num2 + self.num3
#         sub = self.num1 - self.num2 - self.num3
#         mul = self.num1 * self.num2 * self.num3
#         print("addition :-",add)
#         print("subtraction :-", sub)
#         print("multiplication :-", mul)
# obj = derive1()
# obj.read()
# obj.operations()

class radius:
    def read_radius(self):
        self.pi = 3.14
        self.rad = float(input("Enter the radius : "))
class height(radius):
    def read_height(self):
        self.height = float(input("Enter the height : "))
class area(height):
    def area(self):
        result = self.pi * self.rad *2 * self.height
        print("Area of shape :- ", result)
obj=area()
obj.read_radius()
obj.read_height()
obj.area()