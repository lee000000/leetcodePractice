'''
58. Length of Last Word

Given a string s consists of upper/lower-case

alphabets and empty space characters ' ', return

the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence

consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" or s == " ":
            return 0
        n = len(s) - 1
        count = 0
        #while n >= 0:
        while s[n] == " " and n >= 0:
            n -= 1
        while s[n] != " " and n >= 0:
            count += 1
            n -= 1
        return count

    def fasterSolution(self, s):
        return len((s.rstrip(' ').split(" ")[-1]))
