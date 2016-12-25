'''
264. Ugly Number II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only

include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is

the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.
'''
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        ret = [0 for _ in range(n)]
        ret[0] = 1
        mTwo, mThree, mFive = 2, 3, 5
        iTwo = iThree = iFive = 0
        for i in range(1, n):
            minNumAtI = min(min(mTwo, mThree), mFive)
            ret[i] = minNumAtI
            if minNumAtI == mTwo:
                ret[i] = mTwo
                iTwo += 1
                mTwo = 2 * ret[iTwo]
            if minNumAtI == mThree:
                ret[i] = mThree
                iThree += 1
                mThree = 3 * ret[iThree]
            if minNumAtI == mFive:
                ret[i] = mFive
                iFive += 1
                mFive = 5 * ret[iFive]
        return ret[n - 1]


def test():
    n = 10
    sol = Solution()
    print(sol.nthUglyNumber(n))


if __name__ == "__main__":
    test()
