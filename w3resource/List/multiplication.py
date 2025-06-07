#Multiply Items in List
#list = [1,2,3,4]
def mul_num(items):
    num = 1
    for x in items:
        num *= x
    return num
print(mul_num([1,2,9]))

#OR

numbers = [1,2,3,4]
multiplier = 2
result = []
for num in numbers:
    multiplied_list =result.append(num * multiplier)
print("Multiplied list : ",result)
