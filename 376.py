'''
376. Wiggle Subsequence

A sequence of numbers is called a wiggle sequence if the differences

between successive numbers strictly alternate between positive and

negative. The first difference (if one exists) may be either positive

or negative. A sequence with fewer than two elements is trivially a

wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences

(6,-3,5,-7,3) are alternately positive and negative. In contrast,

[1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because

its first two differences are positive and the second because its last

difference is zero.

Given a sequence of integers, return the length of the longest subsequence

that is a wiggle sequence. A subsequence is obtained by deleting some

number of elements (eventually, also zero) from the original sequence,

leaving the remaining elements in their original order.

Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is

[1,17,10,13,10,16,8].

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?
'''
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m < 2:
            return m
        # find the first set of non-equal contiguous numbers
        index = 1
        while not nums[index] - nums[index - 1] and index < m - 1:
            index += 1
        if nums[index] != nums[index - 1]:
            increasing = nums[index] > nums[index - 1]
        else:
            return 1
        count = 2
        # assume f(nums[0 : i - 1]) renders maximum length
        # and the last two numbers indicates an 'increasing' or
        # 'decreasing' pattern
        for i in range(index + 1, m):

            if (increasing and nums[i] < nums[i - 1]) or \
            (not increasing and nums[i] > nums[i - 1]):
                count += 1
                increasing = not increasing
        return count




def test():
    numsSet = [[3,3,3,2,5], [1,1,7,4,9,2,5], []]
    sol = Solution()
    for nums in numsSet:
        print(nums)
        print(sol.wiggleMaxLength(nums))
        print("##########################")


if __name__ == "__main__":
    test()
