'''
300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing

subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length

is 4. Note that there may be more than one LIS combination, it is only

necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

Credits:
Special thanks to @pbrother for adding this problem and creating all test

cases.
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        s = [1 for _ in range(len(nums))]
        maxSoFar = 1
        for i in range(1, len(nums)):
            s[i] += max([s[j] if nums[j] < nums[i] else 0 for j in range(i)])
            maxSoFar = max(s[i], maxSoFar)
            print(s)
            # s[i] += s[j] if nums[j] <= nums[i] for j in range(i)

        return maxSoFar


def test():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    numsb = [1,3,6,7,9,4,10,5,6]
    sol = Solution()
    print(sol.lengthOfLIS(nums))


if __name__ == "__main__":
    test()
