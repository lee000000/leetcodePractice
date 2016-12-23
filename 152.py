'''
152. Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number)

which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

Subscribe to see which companies asked this question
'''
import sys
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # runtime 52ms
        if len(nums) == 1:
            return nums[0]

        maxPro = - sys.maxsize - 1
        minPro = sys.maxsize
        ret = [maxPro, minPro]
        for num in nums:
           if num < 0:
               maxPro, minPro = minPro, maxPro

           maxPro = max(num, maxPro * num)
           minPro = min(num, minPro * num)

           ret[0] = max(ret[0], maxPro)
           ret[1] = min(ret[1], minPro)

        #    print(ret)
        return ret[0]


def test():
    num = [-2,0,-1]
    nums = [2,3,-2,-4]
    sol = Solution()
    print(sol.maxProduct(nums))


if __name__ == "__main__":
    test()
