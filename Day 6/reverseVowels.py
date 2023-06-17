'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Ex.1
Input: s = "hello"
Output: "holle"

Ex.2
Input: s = "leetcode"
Output: "leotcede"
'''


def reverse_vowels(s: str) -> str:
    start = 0
    end = len(s) - 1
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    word = list(s)
    while start < end:
        if word[start] in vowels and word[end] in vowels:
            word[start] = s[end]
            word[end] = s[start]
            start += 1
            end -= 1
        elif word[start] in vowels:
            end -= 1
        elif word[end] in vowels:
            start += 1
        else:
            start += 1
            end -= 1
    return ''.join(word)
