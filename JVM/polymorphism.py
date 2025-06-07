class practice:
    def speaking(self):
       return "i am speaking"
class author(practice):
    def speaking(self):
       return"author speaking"
class result(practice):
    def speaking(self):
        return"everyone speaking"

obj=[author(),result(),practice()]
for value in obj:
    print( value.speaking())