'''
257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        print(root.val)
        if not root.right and not root.left:
            return [str(root.val)]

        a = [str(root.val) + "->" + node for node in self.binaryTreePaths(root.left)]
        a += [str(root.val) + "->"+ node for node in self.binaryTreePaths(root.right)]

        return a
