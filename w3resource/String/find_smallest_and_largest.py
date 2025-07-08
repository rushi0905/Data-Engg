def find_small_large(str):
    word = ""
    all_word = []
    str = str + " "
    for i in range(0,len(str)):
        if(str[i] != ' '):
            word = word + str[i]
        else:
            all_word.append(word)
            word = ""
    small = large = all_word[0]
    for k in range(0, len(all_word)):
        if(len(small)) > len(all_word[k]):
            small = all_word[k]
        if(len(large)) < len((all_word)[k]):
            large = all_word[k]
    return small,large
str = "Write a Java program to sort an array of given integers using Quick sort Algorithm.";
small, large = find_small_large(str)
print("Smallest word: " + small)
print("Largest word: " + large)
