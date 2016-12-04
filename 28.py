'''
28. Implement strStr()

Implement strStr().

Returns the index of the first occurrence of needle in

haystack, or -1 if needle is not part of haystack.
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        if haystack == "":
            return -1

        interval = len(needle)
        for i in range(len(haystack) - interval):
            if haystack[i : i + interval] == needle:
                return i
            else:
                i = i + interval

        return -1
