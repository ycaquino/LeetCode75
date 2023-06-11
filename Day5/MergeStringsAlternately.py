'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other, append the additional letters
onto the end of the merged string.

Return the merged string.

Ex.1
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Ex.2
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"

Ex.3
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
'''


class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        p1 = 0
        p2 = 0
        switch = True

        while p1 < len(word1) and p2 < len(word2):
            if switch:
                result += word1[p1]
                p1 += 1
                switch = False
            else:
                result += word2[p2]
                p2 += 1
                switch = True

        while p1 < len(word1):
            result += word1[p1]
            p1 += 1

        while p2 < len(word2):
            result += word2[p2]
            p2 += 1

        return result
