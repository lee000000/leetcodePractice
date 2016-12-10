'''
202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the

sum of the squares of its digits, and repeat the process until

the number equals 1 (where it will stay), or it loops endlessly

in a cycle which does not include 1. Those numbers for which this

process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
'''
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        dic = {}
        sum = 0
        while sum != 1:
            temp = sum = 0
            while n != 0:
                sum += (n % 10) * (n % 10)
                n //= 10
            n = sum

            if temp == sum or sum in dic.keys():
                return False
            dic[sum] = 1
        if sum == 1:
            return True
        else:
            return False

if __name__ == "__main__":
    n = 20
    sol = Solution()
    print(sol.isHappy(n))
