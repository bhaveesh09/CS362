from programs import palindrome
from wordCount import wordCount
import unittest

class testPalindrome(unittest.TestCase):
    def test_palidrome(self):
        case = palindrome("WOW")
        self.assertEqual(case, True)
    
    def test_palidrome2(self):
        case = palindrome("NOT A PALINDROME")
        self.assertEqual(case, False)
    
    def test_palidrome3(self):
        case = palindrome("")
        self.assertEqual(case, False)

class testWordCount(unittest.TestCase):
    def test_wordCount(self):
        case = wordCount("THERE ARE FOUR WORDS")
        self.assertEqual(case, 4)

    def test_wordCount2(self):
        case = wordCount("There are 4 words")
        self.assertEqual(case, 4)

    def test_wordCount3(self):
        case = wordCount('')
        self.assertEqual(case, 0)

    


if __name__ == '__main__':
    unittest.main()

