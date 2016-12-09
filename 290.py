'''
290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter

in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase

letters separated by a single space.
'''
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        lstr = str.split(" ")
        if len(pattern) != len(lstr):
            return False


        retP = []
        retS = []

        for p in pattern:
            retP.append(pattern.find(p))

        for s in lstr:
            retS.append(lstr.index(s))
        # print(retP)
        # print(retS)
        return (retP == retS)


if __name__ == "__main__":
    pattern = "abba"
    s = "dog dog dog dog"
    sol = Solution()
    print(sol.wordPattern(pattern, s))
