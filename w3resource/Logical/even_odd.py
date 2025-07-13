#Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
num = float(input("Enter the number : "))
mod = num % 2
def even_odd(num):
    if mod == 0:
        print("Number is Even")
    else:
        print("Number is odd")
even_odd(num)

# or
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

