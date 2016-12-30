'''
377. Combination Sum IV

Given an integer array with all positive numbers and no duplicates, find

the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
'''
class Solution(object):
    def combinationSum4_BottomUp(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(1, target + 1):
            for j in range(len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]
        return dp[-1]



    def combinationSum4_TopDown(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [-1 for _ in range(target + 1)]
        dp[0] = 1
        return self.help(nums, target, dp)

    def help(self, nums, target, dp):
        print("+++++++++++++++++++++++++++++")
        print(dp)
        print(target)
        if dp[target] != -1:
            return dp[target]

        count = 0
        for i in range(len(nums)):
            if target >= nums[i]:
                count += self.help(nums, target - nums[i], dp)

        dp[target] = count
        return count


    # naive recursion
    def combinationSum4_slow(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # TLE when nums = [4, 2, 1], target = 32
        if target == 0:
            return 1
        count = 0
        for num in nums:
            if target >= num:
                count += self.combinationSum4(nums, target - num)

        return count


def test():
    # nums = [4, 2, 1]
    # target = 32
    nums = [1, 2]
    target = 5
    sol = Solution()
    print(sol.combinationSum4_TopDown(nums, target))

if __name__ == "__main__":
    test()
