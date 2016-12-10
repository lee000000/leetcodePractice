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
=======
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
>>>>>>> aa3a3a394a8aea35c5a9286b32a9b0119d21a7a7


if __name__ == "__main__":
    nums1 = [1]
    nums2 = [1, 2]
    sol = Solution()
    print(sol.intersection(nums1, nums2))
