'''
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest

path from the root node down to the nearest leaf node.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        i = 0
        frontier = [root]
        while root and frontier:
            i += 1
            for node in frontier:
                # print(node.val)
                if not node.left and not node.right:
                    return i
            lrPairs = [(node.left, node.right) for node in frontier]

            frontier = [n for pair in lrPairs for n in pair if n]
            # print([x.val for x in frontier])
        return i
