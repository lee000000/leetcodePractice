'''
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself

(ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True


        return isSymmetricH(root.left, root.right)


    def isSymmetricH(self, p, q):
        if not p and not q: # leaf
            return True
        if not p or not q: # a node with either left or right child
            return False
        return (p.val == q.val) and self.isSymmetricH(p.left, q.right) and isSymmetricH(p.right, q.left)
