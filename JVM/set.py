set1={1,2,3,3,4}
set2={4,5,6,7}
set_list = {list['qwe','ert',89]}
print(set_list)
print(set1|set2)
print(set1&set2)
print("set1=",set1)
print("set2",set2)
print("Difference=",set1-set2)
print("Difference=",set2-set1)
print("symmetric difference=",set1^set2)
set1.add(90,)
print(set1)
set1.remove(101,3)
set1.discard(101)

set4=frozenset([9,5,6,7])
print(set4)