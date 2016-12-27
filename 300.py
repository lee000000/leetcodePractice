'''
300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing

subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length

is 4. Note that there may be more than one LIS combination, it is only

necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

Credits:
Special thanks to @pbrother for adding this problem and creating all test

cases.
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        s = [1 for _ in range(len(nums))]
        maxSoFar = 1
        for i in range(1, len(nums)):
            s[i] += max([s[j] if nums[j] < nums[i] else 0 for j in range(i)])
            maxSoFar = max(s[i], maxSoFar)
            print(s)
            # s[i] += s[j] if nums[j] <= nums[i] for j in range(i)

        return maxSoFar

    # From GeeksForGeeks: O(NlogN)
    def lengthOfLISBinary(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # endArray keeps track of the largest element of the
        # active arrays starting with each num in nums
        endArray = [0 for _ in range(len(nums))]
        endArray[0] = nums[0]
        endI = 1 # always points to the next emplty ending element's position
        for i in range(1, len(nums)):
            if nums[i] < endArray[0]: # nums[i] is less than the smallest
                # start a new array
                endArray[0] = nums[i]
            elif nums[i] > endArray[endI - 1]: # nums[i] is larger than the biggest
                # extend the end array
                endArray[endI] = nums[i]
                endI += 1
            else:
                # find the index of the ceil element for nums[i]
                index = self.ceilIndex(endArray, -1, endI - 1, nums[i])
                # replace the ending element with the new one
                endArray[index] = nums[i]
        #print(endArray)
        return endI


    def ceilIndex(self, array, l, r, key):
        # binary search for key
        while l < r - 1:
            print((l, r))
            m = l + (r - l) // 2
            if array[m] < key:
                l = m
            else:
                r = m
        return r


def test():
    numsa = [10, 9, 2, 5, 3, 7, 101, 18]
    numsb = [2, 5, 3, 7, 11, 8, 10, 13, 6] # --> 6
    nums = [4,10,4,3,8,9]
    sol = Solution()
    print(sol.lengthOfLISBinary(nums))

def testBinary():
    a = [1, 1, 3, 5, 6]
    l = 0
    r = len(a) - 1
    sol = Solution()
    print(sol.ceilIndex(a, l , r, 4))


if __name__ == "__main__":
    test()
