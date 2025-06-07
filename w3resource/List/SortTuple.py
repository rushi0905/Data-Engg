#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

def sort_by_last_element(tuples_list):
    return sorted(tuples_list,key=lambda x:x[-1])

tuples_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = sort_by_last_element(tuples_list)
print(sorted_list)


'''
def quickSort(list):
    pivot = list[0](1)
    
    # if (comparator(pivot, ))
def comparator(a, b):
    lastElementofA = a(1) #5
    lastElementOfB = b(1) #2
    
    if lastElementofA == lastElementOfB:
        return 0
    if lastElementofA < lastElementOfB:
        return -1
    else:
        return 1
'''