def test_distinct(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False
print(test_distinct([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(test_distinct([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]))