'''
219. Contains Duplicate II

Given an array of integers and an integer k, find out

whether there are two distinct indices i and j in the array

such that nums[i] = nums[j] and the difference between i and j is at most k.
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for count, num in enumerate(nums):
            if (num in dic.keys() and count - dic[num] <= k):
                    return True
            dic[num] = count
        return False




if __name__ == "__main__":
    a = [1, 0, 1, 1]

    sol = Solution()
    print(sol.containsNearbyDuplicate(a, 1))
