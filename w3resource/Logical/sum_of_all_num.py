num = [10,23,445,67,89,90,100]
def sum_of_all_num(num):
    total = 0
    for n in num:
        total += n
    return total
print(sum_of_all_num(num))  # Output: 1024