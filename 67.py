'''
67. Add Binary

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if (a == ""):
            return b
        if (b == ""):
            return a

        bin_a = int(a, 2)
        bin_b = int(b, 2)

        ret = bin_a + bin_b
        return bin(ret)[2:]
