'''
125. Valid Palindrome

Given a string, determine if it is a palindrome,

considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a

good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return True

        start = 0
        end = len(s) - 1
        while start < end:
            while not s[start].isalnum() and start < end:
                start += 1
            while not s[end].isalnum() and start < end:
                end -= 1
            # print((start, end))
            # print((s[start], s[end]))
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True

if __name__ == "__main__":
    s = "a."
    sol = Solution()
    print(sol.isPalindrome(s))
