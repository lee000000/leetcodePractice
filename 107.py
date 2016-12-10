'''
107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of

its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # stack bfs, similar to bfs + reverse
        ans = []
        frontier = [root]
        stack = []
        while root and frontier:
            stack.append([node.val for node in frontier])
            nxt = [(node.left, node.right) for node in frontier]
            frontier = [node for nd in nxt for node in nd if node]

        while stack:
            ans.append(stack.pop())

        return ans
