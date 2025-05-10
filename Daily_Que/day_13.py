#Remove and add item in a list
from collections import Counter
from operator import countOf

list1 = [54, 44, 27, 79, 91, 41]
# list1.remove(54)
remove_ele=list1.pop(2)
print(remove_ele)
del(list1[2])
print(list1)
list1.append(34)
print(list1)

print('\n','**********************************************************************************************')

#Count the occurrence of each element from a list
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

count = 0
for val in sample_list:
    if val == 45:
        count += 1
print(count)
#or
print(sample_list.count(11))
#0r
use_collector = Counter(sample_list)
print(use_collector[45])

print('\n','**********************************************************************************************')

#Create a Python set such that it shows the element from both lists in a pair
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
pair_set = set(zip(first_list,second_list))
print(pair_set)
#or
pairs = [(x,y) for x in first_list for y in second_list if x != y]
print(pairs)

print('\n','**********************************************************************************************')

#Find the intersection (common) of two sets and remove those elements from the first set
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

comman_ele = first_set.intersection(second_set)
print(comman_ele)

first_set.difference_update(comman_ele)
print(first_set)

print('\n','**********************************************************************************************')

#Remove duplicates from a list and create a tuple and find the minimum and maximum number
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

unique_set = set(sample_list)
unique_tuple = tuple(unique_set)
min_val = min(unique_tuple)
max_val = max(unique_tuple)
print("Tuple without duplicates:", unique_tuple)
print("Minimum value:", min_val)
print("Maximum value:", max_val)

print('\n','**********************************************************************************************')

