#Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.

List = ['abc','xyz','aba',1221]
def match_word(words):
    ctr = 0
    for word in words:
        if len(words)>1 and word[0] == word[-1]:
            ctr +=1
    return ctr
print(match_word(['abc','xyz','aba','1221']))
###################################################################

#Count Strings Where the First Character Appears More Than Once
def count_repeating_first_char(strings):
    count = 0
    for s in strings:
        if len(s) > 1 and s.count(s[0]) > 1:
            count +=1
    return count
listofwords = ['apple','banana','cherry','amber','coconut']
print(count_repeating_first_char(listofwords))

#Write a Python program to count words that contain at least one vowel and start and end with the same letter.

