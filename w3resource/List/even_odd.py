class even_odd:

    def find_even_odd_num_from_list(self, numbers):
        even_num = []
        odd_num = []

        for i in numbers:
            if i % 2 == 0:
                even_num.append(i)
            else:
                odd_num.append(i)
        return even_num, odd_num

# Create an object of the class
obj = even_odd()

# Provide the list
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 3, 233]

# Call the method on the object
even, odd = obj.find_even_odd_num_from_list(numbers_list)

# Print results
print("Even numbers:", even)
print("Odd numbers:", odd)
