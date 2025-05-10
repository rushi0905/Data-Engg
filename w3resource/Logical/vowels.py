#Write a Python program to test whether a passed letter is a vowel or not.
def is_vowel(char):
    all_vowel = 'aeiou'
    return char in all_vowel
print(is_vowel('c'))
print(is_vowel('a'))