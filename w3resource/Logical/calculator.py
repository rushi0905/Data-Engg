#Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

def sum_thrice(x,y,z):
    sum = x+y+z
    if x==y==z:
        sum = sum*3
    return sum
print(sum_thrice(1,3,4))
print(sum_thrice(3,3,3))