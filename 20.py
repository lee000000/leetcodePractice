'''
20. Valid Parentheses

Given a string containing just the characters

'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}"

are all valid but "(]" and "([)]" are not.
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        if len(s) % 2 == 1:
            return False

        ret = []
        ret.append(s[0])
        for i in s[1:]:
            if len(ret) == 0 or self.reverse(i) != ret[-1]:
                ret.append(i)
            else:
                ret.pop()
        if len(ret) == 0:
            return True
        else:
            return False

    def reverse(self, b):
        if b == "(":
            return ")"
        elif b == ")":
            return "("
        elif b == "[":
            return "]"
        elif b == "]":
            return "["
        elif b == "{":
            return "}"
        elif b == "}":
            return "{"
        else:
            return None

if __name__ == "__main__":
    a = "({[]})"
    sol = Solution()
    print(sol.isValid(a))
