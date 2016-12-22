'''
213. House Robber II


Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new

place for his thievery so that he will not get too much attention. This time,

all houses at this place are arranged in a circle. That means the first house is

the neighbor of the last one. Meanwhile, the security system for these houses

remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each

house, determine the maximum amount of money you can rob tonight without alerting

the police.
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dummyNums = nums + nums
        maxSum = 0
        # startIndex = len(nums)
        for i in range(0, len(nums)):
            print(i)
            # the max of rob house with num or not robbing house with num
            maxSum = max(self.robSingle(dummyNums, i + 2, len(nums) + i - 1),
                        self.robSingle(dummyNums, i + 1, len(nums) + i), maxSum)

        return maxSum



    def robSingle(self, nums, start, end):
        """
        This is the helper function
        & rob a non-circular list of houses as House Robber I
        """
        # print((start, end))
        # print(nums[start: end])
        curMax = 0
        preMax = 0
        for num in nums[start:end]:
            preMax, curMax = curMax, max(curMax, preMax + num)
        # print(curMax)
        # print("####################################")
        return curMax


def test():
    nums = [1, 2, 3, 4, 5]
    sol = Solution()
    print(sol.rob(nums))


if __name__ == "__main__":
    test()
