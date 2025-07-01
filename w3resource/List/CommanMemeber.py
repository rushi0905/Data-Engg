#11. Check Common Member Between Two Lists
def common_data(list1,list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))

def count_comman_element(list3,list4):
    set1 = set(list3)
    set2 = set(list4)
    common_elements = set1.intersection(set2)
    return len(common_elements)
list3 = [1,23,3,34,45,55,65]
list4 = [1,23,344,22,55,2322,211,233]
count = count_comman_element(list3,list4)
print(f"Number of common elements : {count}")


from collections import Counter

def common_elements_with_duplicates(list5, list6):
    # Count elements in both lists
    counter1 = Counter(list5)
    counter2 = Counter(list6)

    # Find intersection including duplicates
    common = counter1 & counter2

    # Expand the intersection to include repeated elements
    result = list(common.elements())
    return result

# Example usage
list5 = [1, 2, 2, 3, 4, 5]
list6 = [2, 2, 3, 6]

common = common_elements_with_duplicates(list5, list6)
print("Common elements including duplicates:", common)


