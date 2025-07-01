def max_min(Data):
    l = Data[0]
    s = Data[0]
    for i in Data:
        if i > l:
            l = i
        if i < s:
            s = i
    return l, s
print(max_min([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
