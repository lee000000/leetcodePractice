'''
448. Find All Numbers Disappeared in an Array


Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),

some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this

array.

Could you do it without extra space and in O(n) runtime? You may assume

the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            if num > 0:
                if nums[num - 1] > 0:
                    nums[num - 1] = -nums[num - 1]
            else:
                if nums[-num - 1] > 0:
                    nums[-num - 1] = -nums[-num - 1]


        output = []
        i = 0
        while i < len(nums):
            if nums[i] > 0:
                output.append(i+1)
            i += 1

        return output

def test():
    a = [1, 1]
    sol = Solution()
    ret = sol.findDisappearedNumbers(a)
    print(ret)

if __name__ == "__main__":
    test()
