
def comman_char(str1,str2):

    set1 = set(str1)
    set2 = set(str2)

    comman = set1 & set2
    if comman:
        result = ''.join(sorted(comman))
        print("Comman characters :", result)
    else:
        print("No common characters found.")
str1 = "DataFrame"
str2 = "FrameWork"

comman_char(str1, str2)