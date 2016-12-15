'''
337. House Robber III

The thief has found himself a new place for his thievery again.

There is only one entrance to this area, called the "root."

Besides the root, each house has one and only one parent house.

After a tour, the smart thief realized that "all houses in this

place forms a binary tree". It will automatically contact the

police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight

without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 1. good DP
        ret = self.robHelper(root)
        return max(ret[0], ret[1])


    def robHelper(self, root):
        if not root:
            return [0, 0]

        ret = [None, None]

        # if the root node is not robbed
        # then the left node and the right node can be
        left = self.robHelper(root.left)
        right = self.robHelper(root.right)

        ret[0] = max(left[0], left[1]) + max(right[0], right[1])
        ret[1] = root.val + left[0] + right[0]

        return ret

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def rob2(self, root):
        # 2. naive DP
        # TLE, also not good
        dic = {}
        return self.robH(root, dic)


    def robH(self, root, dic):
        if not root:
            return 0
        if root in dic.keys():
            return dic[root]

        maxRob = 0

        if root.left:
            maxRob += self.robH(root.left.left, dic) + self.robH(root.left.right, dic)
        if root.right:
            maxRob += self.robH(root.right.left, dic) + self.robH(root.right.right, dic)

        maxRob = max(maxRob + root.val, self.robH(root.left, dic) + self.robH(root.right, dic))


        dic[root] = maxRob
        return maxRob


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def rob3(self, root):
        # 3. naive recursive way
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val

        maxRob = 0
        if root.left:
            maxRob += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            maxRob += self.rob(root.right.left) + self.rob(root.right.right)

        return max(maxRob + root.val, self.rob(root.left) + self.rob(root.right))
