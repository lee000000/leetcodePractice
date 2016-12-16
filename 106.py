'''
106. Construct Binary Tree from Inorder and Postorder Traversal


Given inorder and postorder traversal of a tree, construct the

binary tree.

Note:
You may assume that duplicates do not exist in the tree.
preorder = [7,10,4,3,1,2,8,11]
* inorder = [4,10,3,1,7,11,8,2]
* postorder = [4,1,3,10,11,8,2,7]
        ___7___
       /     \
    10        2
   /   \      /
  4    3      8
        \    /
         1  11
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# runtime 255ms
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # use post oder last element -- root node of the tree
        # locate in inorder position;
        # left to the node is the left subtree
        # right to the node is the right subtree;
        # the recursion order is important;
        # postorder is necessary, right, left;
        # Because this should be in the reversed order of
        # taking nodes off the tree
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())

        i = inorder.index(root.val)
        leftIn = inorder[0 : i]

        rightIn = inorder[i + 1 : ]

        root.right = self.buildTree(rightIn, postorder)
        root.left = self.buildTree(leftIn, postorder)

        return root


    # def buildHelp(self, inorder, postorder, root):
