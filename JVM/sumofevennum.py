class add:

    def adds(self,num):
        for var in range(0,num,2):
            sum = 0
            sum = sum+var
        print(sum)
    obj=adds()
    num = int(input("Enter the num:"))
    obj.adds(num)

    def add1(val):
        sum1 = 0
        for var in range(0, val, 2):
            sum1 = sum1 + var
            print(var)
        print("sum", sum1)

    num = int(input("Enter the num:"))
    add1(num)

    # def add(self,num):