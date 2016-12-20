'''
95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's

(binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # runtime 99ms average
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.help(1, n)


    def help(self, s, e):
        res = []
        if s > e:
            res.append(None)
            return res

        i = s
        while i <= e:
            left = self.help(s, i - 1)
            right = self.help(i + 1, e)
            for nodeL in left:
                for nodeR in right:
                    root = TreeNode(i)
                    root.left = nodeL
                    root.right = nodeR
                    res.append(root)
            i += 1

        return res
