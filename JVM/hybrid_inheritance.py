class show1:
    def length(self):
        self.len = float(input("Enter the length : "))

class show2(show1):
    def breadth(self):
        self.bdh = float(input("Enter the breadth : "))

class show3(show2):
    def height(self):
        self.ht = float(input("Enter the height : "))

class result(show3):
    def volume(self):
        self.vol = self.len * self.bdh * self.ht
        print("The vol is : ",self.vol)

obj = result()
obj.length()
obj.breadth()
obj.height()
obj.volume()