'''
108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order,

convert it to a height balanced BST.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 130 - 150 ms 
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(None)
        return self.help(nums, root)


    def help(self, nums, root):
        if (not nums):
            return None

        root = TreeNode(nums[len(nums)/2])
        root.left = self.help(nums[0 : len(nums)/2], root)
        root.right = self.help(nums[(len(nums) / 2 + 1) : ], root)

        return root
