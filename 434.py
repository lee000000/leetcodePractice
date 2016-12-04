'''
434. Number of Segments in a String

Count the number of segments in a string, where a segment

is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-#printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
'''
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        if (len(s) == 1 and s != " "):
            return 1

        if (len(s) == 1 and s == " "):
            return 0

        count = 0
        for i in range(len(s)):
            #print("\'", s[i],"\'")
            if s[i] == " " and s[i - 1] != " ":
                #print("here")
                count += 1
        if s[0] != " " and s[-1] != " ":
            count += 1
        return count

if __name__ == "__main__":
    a = "Of all the gin joints in all the towns in all the world,   "
    sol = Solution()
    print(sol.countSegments(a))
