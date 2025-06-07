class principal:
    def __init__(self):
        self.principl = float(input("Enter the amount = "))


class rate:
    def __init__(self):
        self.rates = float(input("Enter the rate = "))


class interset(principal, rate):
    def __init__(self):
        principal.__init__(self)
        rate.__init__(self)
        self.time = float(input("Enter the time = "))

    def calculate(self):
        si = (self.principl * self.rates * self.time) / 100
        print("simple interest=", si)


obj = interset()
obj.calculate()