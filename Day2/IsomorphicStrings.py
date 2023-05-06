'''
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Ex. 1:
Input: s = "egg", t = "add"
Output: true

Ex. 2:
Input: s = "foo", t = "bar"
Output: false

Ex. 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        result, mapping, mapped = [], {}, set()
        for i in range(len(s)):
            if (s[i] not in mapping) and (t[i] not in mapped):
                mapping[s[i]] = t[i]
                mapped.add(t[i])
            elif s[i] not in mapping and t[i] in mapped:
                mapping[s[i]] = ''
            result.append(mapping[s[i]])
        return ''.join(result) == t