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

        ret = []
        dic1 = {}
        dic2 = {}
        for s in nums1:
            if s in dic1.keys():
                dic1[s] = dic1[s] + 1
            else:
                dic1[s] = 1

        for l in nums2:
            if l in dic2.keys():
                dic2[l] = dic2[l] + 1
            else:
                dic2[l] = 1

        for k in dic2:
            if k in dic1.keys():
                ret.append(k)

        return ret



        #return list(set(nums1).intersection(set(nums2)))


if __name__ == "__main__":
    nums1 = [1]
    nums2 = [1, 2]
    sol = Solution()
    print(sol.intersection(nums1, nums2))
