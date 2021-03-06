'''
392. Is Subsequence

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in

both s and t. t is potentially a very long (length ~= 500,000)

string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from

the original string by deleting some (can be none) of the characters

without disturbing the relative positions of the remaining characters.

(ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B,

and you want to check one by one to see if T has its subsequence.

In this scenario, how would you change your code?
'''
class Solution(object):
    def isSubSequence_2(self, s, t):
        if len(t) < len(s):
            return False

        for l in s:
            temp = t.find(l)
            if temp == -1:
                return False
            t = t[temp + 1:]
        return True


    # runtime 392 ms
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        jt = 0
        js = 0
        while jt < len(t) and js < len(s):
            while t[jt] != s[js] and jt < len(t) - 1:
                print(t[jt])
                jt += 1
            jt += 1
            js += 1

        if js < len(s):
            return False
        else:
            return True


def test():
    s = "abc"
    t = "ahgbdc"
    sol = Solution()
    print(sol.isSubSequence_2(s, t))


if __name__ == "__main__":
    test()
