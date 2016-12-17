'''
105. Construct Binary Tree from Preorder and Inorder Traversal


Given preorder and inorder traversal of a tree, construct

the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
* preorder = [7,10,4,3,1,2,8,11]
* inorder = [4,10,3,1,7,11,8,2]
postorder = [4,1,3,10,11,8,2,7]
        ___7___
       /       \
    10          2
   /   \       /
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

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        * preorder = [7,10,4,3,1,2,8,11]
        * inorder = [4,10,3,1,7,11,8,2]
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        dic = {}
        for i, val in enumerate(inorder):
            dic[val] = i
        return self.buildHelp(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, dic)


    def buildHelp(self, preorder, ps, pe, inorder, iis, ie, dic):
        if ps > pe or iis > ie:
            return None

        root = TreeNode(dic[preorder[ps]])
        i = inorder[root.val]

        left = self.buildHelp(preorder, ps + 1, i + 1, inorder, iis, i, dic)
        right = self.buildHelp(preorder, i + 1, pe, inorder, i + 1, ie, dic)
        root.left = left
        root.right = right
        return root


    def buildTree_naiveRecursive(self, preorder, inorder):
            if inorder:
            root = TreeNode(preorder.pop(0))
            i = inorder.index(root.val)

            root.left = self.buildTree(preorder, inorder[:i])
            root.right = self.buildTree(preorder, inorder[i + 1:])
            return root
