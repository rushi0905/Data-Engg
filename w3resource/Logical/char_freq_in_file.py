import collections
import pprint

# Python program to count the frequency of characters in a file
file_input = input("Enter the file name: ")
with open(file_input,'r') as info:
    count = collections.Counter(info.read().upper())
    value = pprint(pprint.pformat(count))
print(value)