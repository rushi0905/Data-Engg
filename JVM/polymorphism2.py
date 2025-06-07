class read:
    def values(self):
        self.num1 = int(input("Enter the num : "))
        self.num2 = int(input("Enter the num : "))

class printData(read):
    def values(self):
        super().values()
        self.add = self.num1 + self.num2
        print("Addition : ",self.add)

obj =printData()
obj.values()
