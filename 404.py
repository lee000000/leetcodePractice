'''
404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values

9 and 15 respectively. Return 24.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if root:
        #     print(root.val)
        if not root:
            return 0

        sum = 0
        if root.left:
            if not root.left.left and not root.left.right: # Found left leaf
                # print("here", root.left.val)
                sum += root.left.val

        return sum + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

        # First Trial wrong
        # if not root:
        #     return 0
        #
        # sum = 0
        # if not root.left and not root.right:
        #     return root.val
        #
        # if not root.left.left and not root.left.right:
        #     sum += root.left.val
        #     return sum
        #
        # return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
