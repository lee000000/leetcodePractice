'''
414. Third Maximum Number


Given a non-empty array of integers, return the third maximum number

in this array. If it does not exist, return the maximum number. The time

complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is

returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum

distinct number.

Both numbers with value 2 are both considered as second maximum.
'''
import sys
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        first = second = third = min_val = -sys.maxsize - 1

        #dic = {"first": min_val, "second": min_val, "thrid": min_val}

        for num in nums:
            if num > third and num < second:
                third = num
            elif num > second and num < first:
                third = second
                second = num
            elif num > first:
                first, second, third = num, first, second
            else:
                continue
        #print((first, second, third))
        if len(set((first, second, third))) == 3 and third != min_val:
            return third
        else:
            return first



def test():
    a = [1, 1, 2]
    sol = Solution()
    lst = sol.thirdMax(a)
    print(lst)


if __name__ == "__main__":
    test()
