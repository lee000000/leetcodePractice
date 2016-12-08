'''
350. Intersection of Two Arrays II


Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited
such that you cannot load all elements into the memory at once?
'''
class Solution(object):
    def intersect(self, nums1, nums2):
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
                while dic1[k] != 0 and dic2[k] != 0:
                    ret.append(k)
                    dic1[k] -= 1
                    dic2[k] -= 1

        return ret

    def intersectII(self, nums1, nums1):
        dic1 = collections.Counter(nums1)
        dic2 = collections.Counter(nums2)
        # for k in dic2:
        #     if k in dic1.keys():
        #         while dic1[k] != 0 and dic2[k] != 0:
        #             ret.append(k)
        #             dic1[k] -= 1
        #             dic2[k] -= 1

        return list((dic1 & dic2).elements())
