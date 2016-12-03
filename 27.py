'''
27. Remove element

Given an array and a value, remove all instances of that

value in place and return the new length.

Do not allocate extra space for another array, you must do

this in place with constant memory.

The order of elements can be changed. It doesn't matter what

you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements

of nums being 2
'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        i = 0
        n = len(nums)
        while i < n:
            if (nums[i] ^ val == 0):
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1

        return n

if __name__ == "__main__":
    a = [[3, 2, 2, 2, 3], 3]
    sol = Solution()
    ret = sol.removeElement(a[0], a[1])
    print(ret)
