# Write a Python program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
import sys
from datetime import datetime
from math import pi
from platform import python_version

from trio import current_time

print("Twinkle, twinkle, little star,\n\t How I wonder what you are! \n\t\t Up above the world so high,\n\t\t Like a diamond in the sky. \n Twinkle, twinkle, little star,\n\t How I wonder what you are")
print('*'* 80)
print(sys.version)
print(sys.version_info)
print("Python Version is ",python_version())
print('*'* 80)

now = datetime.now()
print("Current date and time")
print('\n',now.strftime("%Y-%M-%D %H:%M:%S"))

print('*'* 80)

# Area of circle
#r=1.1
r = float(input("Enter the radius of circle : "))
# pie = 3.14

area_of_circle = pi * r * r
print(area_of_circle)
print('*'* 80)

lst = [1,2,3,4,5,6]
rev_lst = lst.reverse()
print(lst)
