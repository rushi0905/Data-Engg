new_list= [12,36,45,99,10001]
max_num = new_list[0]
for item in new_list:
    if item > max_num:
        max_num = item
print("greatest num in list",max_num)


def max_num_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a

    return max
print(max_num_list([-2,25,78,-55]))
