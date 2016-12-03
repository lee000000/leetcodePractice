'''
268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,

find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement

it using only constant extra space complexity?

'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 0):
            return 0

        sumA = 0
        for i in range(len(nums) + 1):
            sumA += i

        sumB = 0
        for num in nums:
            sumB += num

        return (sumA - sumB)

    def missingNumberB(self, nums):
            n = len(nums)
            return reduce(operator.xor, nums) ^ [n, 1, n+1, 0][n % 4]

    if __name__ == "__main__":
        a = [0, 1, 3, 4, 5, 6]
        sol = Solution()
        ret = sol.missingNumber(a)
        print(ret)
