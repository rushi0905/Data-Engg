# Find the list of words that are longer than n from a given list of words
from w3resource.String.string_ops import result


def long_word(n,str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
print(long_word(3,'length of string'))


def find_word_of_length(n,words):
    return [word for word in words if len(word)==n]
    word_list = ['apple', 'bat', 'carrot', 'dog', 'egg', 'fish']
    n=3
    result = find_word_of_length(word_list,n)
    print(f"words with exactly {n} characters : {result}")

