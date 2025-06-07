def smallest_num_list(list):
    small = list[0]
    for item in list:
        if item < small:
            small = item
    return small
print("Smallest item in list: ",smallest_num_list([1,2,3,-4]))

#OR

small_list = [-8,-9,12,23]
small_num = small_list[0]
for num in small_list:
    if small_num < num:
        num = small_num
print("smallest num in list",small_num)

#Write a Python program to find the second smallest number in a list.
def second_smallest(lst):
    small = float('inf')
    second_small = float('inf')
    for number in lst:
        if number < small:
            second_small = small
            small = number
        elif small < number < second_small:
            second_small = number
    return second_small if second_small != float('inf') else None
numbers = [1,2,3,4,5]
print("Second smallest number: ",second_smallest(numbers))


