'''
169. Majority Element


Given an array of size n, find the majority element. The majority element is the

element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist

in the array.
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return nums[0] if nums else None

        dic = {}
        for num in nums:
            if not num in dic.keys():
                dic[num] = 1
            else:
                dic[num] += 1

        bar = len(nums) // 2

        for k, v in dic.items():
            if v > bar:
                return k
        return nums[0]


def test():
    nums = [1, 2, 2, 1, 2]
    sol = Solution()
    print(sol.majorityElement(nums))


if __name__ =="__main__":
    test()
