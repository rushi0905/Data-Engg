class datainput:
    def show(self):
        self.length = float(input("Enter the lenght = "))
        self.breadth = float(input("Enter the breadth = "))
        self.height = float(input("Enter the height = "))

class volume(datainput):
    def result(self):
        self.vol = self.length*self.breadth*self.height
        print("The volume is : ",self.vol)

class area(datainput):
    def show2(self):
        self.ar = self.length*self.breadth
        print("The area is : ",self.ar)

obj=volume()
obj.show()
obj.result()
obj2=area()
obj2.show()
obj2.show2()

print("***************************************************************************************************")


class Datainput:
    def __init__(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h

    def show(self):
        print("Length:", self.l)
        print("Breadth:", self.b)
        print("Height:", self.h)


class Volume(Datainput):
    def result(self):
        Datainput.__init__(self, l, b, h)
        print("Volume =", self.l * self.b * self.h)


class Area(Datainput):

    def show(self):
        Datainput.__init__(self, l, b, h)
        print("Area =", self.l * self.b)


l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
h = int(input("Enter height: "))

obj = Volume(l, b, h)
obj.show()
obj.result()
obj = Area(l, b, h)
obj.show()