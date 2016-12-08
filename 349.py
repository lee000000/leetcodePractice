'''
349. Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
[3, 2, 2, 1] [2, 1]    [2, 1]

Note:
Each element in the result must be unique.
The result can be in any order.
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # ret = []
        # for s in nums[2]:
        #     if s in nums1:
        #         ret.append(s)
        # i = len(ret) - 1
        # if i == 0 or i == 1:
        #     return ret
        # else:
        #     while i >= 0:
        #         temp = ret[0 : i + 1].pop()
        #         if temp not in ret:
        #             ret.append(temp)
        #         i -= 1
        # return ret[i:]

        return list(set(nums1).intersection(set(nums2)))


if __name__ == "__main__":
    nums1 = [1]
    nums2 = [1, 2]
    sol = Solution()
    print(sol.intersection(nums1, nums2))
