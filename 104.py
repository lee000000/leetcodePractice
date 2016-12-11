'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest

path from the root node down to the farthest leaf node.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        height = {root:0,}
        level = [root]

        while level:
            for node in level:
                if node not in height.keys():
                    height[node] = 1
                if node.left:

                    height[node.left] = height[node] + 1

                if node.right:
                    height[node.right] = height[node] + 1


            nxt = [(node.left, node.right) for node in level]

            level = [nd for nodeLR in nxt for nd in nodeLR if nd]


        h = max([h for h in height.values()])
        print(h)
        # print(list((x.val, y) for x, y in height.items()))

        return h + 1
