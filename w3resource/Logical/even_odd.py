#Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
num = float(input("Enter the number : "))
mod = num % 2
def even_odd(num):
    if mod >= 0:
        print("Number is Even")
    else:
        print("Number is odd")
even_odd(num)