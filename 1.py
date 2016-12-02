'''
1. Two Sum


Given an array of integers, return indices of the two numbers such that

they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the

above updated description carefully.
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            print(nums[i])
            if (target - nums[i]) not in dic.keys():
                dic[nums[i]] = i
                print(dic[nums[i]])
            else:
                return [dic[target - nums[i]], i]
            i += 1


if __name__ == "__main__":
    a = [[3,2,4], 6]
    sol = Solution()
    lst = sol.twoSum(a[0], a[1])
    print(lst)
