import unittest
import reverseVowels


class TestReverseVowels(unittest.TestCase):
    def test_reverse_vowels(self):
        self.assertEqual(reverseVowels.reverse_vowels('hello'), 'holle')
        self.assertEqual(reverseVowels.reverse_vowels('leetcode'), 'leotcede')
        self.assertEqual(reverseVowels.reverse_vowels('.,'), '.,')


if __name__ == '__main__':
    unittest.main()
