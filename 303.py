'''
303. Range Sum Query - Immutable


Given an integer array nums, find the sum of the elements

between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        dic = {-1:0,}
        for i, val in enumerate(nums):
            dic[i] = val + dic[i - 1]
        print(dic)
        self.sumIndex = dic

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumIndex[j] - self.sumIndex[i - 1]




# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

def test():
    nums = [-2, 0, 3, -5, 2, -1]
    numArray = NumArray(nums)
    print(numArray.sumRange(0, 1))
    print(numArray.sumRange(1, 2))
    print(numArray.sumRange(0, 2), "1")
    print(numArray.sumRange(2, 5), "-1")
    print(numArray.sumRange(0, 5), "-3")


if __name__ == "__main__":
    test()
