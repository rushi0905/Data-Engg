#Write a Python program to calculate the length of a string.

def len_string(str1):
    count = 0
    for char in str1:
        count +=1
    return count
print(len_string("Rushikesh becomes a data engineer"))
