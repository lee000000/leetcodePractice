'''
198. House Robber

You are a professional robber planning to rob houses along a street.

Each house has a certain amount of money stashed, the only constraint

stopping you from robbing each of them is that adjacent houses have

security system connected and it will automatically contact the police

if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money

of each house, determine the maximum amount of money you can rob tonight

without alerting the police.
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. Basic DP
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0], nums[1]))
        for num in nums[2:]:
            dp.append(max(dp[-1], dp[-2] + num))

        return dp[-1]

        # 2. Improvded DP
    def robImprove(self, nums):
        if not nums:
            return 0
        last = maxsum = 0
        for num in nums:
            last, maxsum = maxsum, max(last + num, maxsum)
        return maxsum


def test():
    nums = [1, 2, 3, 4, 5, 6, 7]
    sol = Solution()
    print(sol.rob(nums))


if __name__ == "__main__":
    test()
