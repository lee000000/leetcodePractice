'''
100. Same Tree

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical

and the nodes have the same value.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True

        if not (p and q):
            return False
        # leaves
        if not p.left and not p.right and not q.left and not q.right:
            if p.val == q.val:
                return True
            else:
                return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and  self.isSameTree(p.right, q.right) 
