#Get a single string from two given strings, separated by a space and swap the first two characters of each string
def char_mix_up(a,b):
    str = 'abc','xyz'
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + ' ' + new_b
print(char_mix_up('abc','xdf'))