class input_data:
    def values(self):
        self.num1 = float(input("Enter the first value : "))
        self.num2 = float(input("Enter the second value : "))
        self.num3 = float(input("Enter the third value : "))

class output(input_data):
    def average(self):
        self.avg = (self.num1 + self.num2 + self.num3) /3
        print("Ave : ",self.avg)

    def percentage(self):
        self.per =  (self.num1 + self.num2 + self.num3)/300 * 100
        print("% : ", self.per)

obj = output()
obj.values()
obj.average()
obj.percentage()