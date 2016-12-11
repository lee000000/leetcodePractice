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


    def levelOrderBottom(self, root):
        # Find the height of the tree
        h = self.heightOf(root)






    def levelOrderBottom(self, root):
        answ, L = [], [root]
        while L and root:
            answ.insert(0,[n.val for n in L])
            L = [ C for N in L for C in (N.left,N.right) if C ]
        return answ

    def heightOf(self, root):
        dic = {}
        level = [root]
        while root and level:
            for node in level:
                if node in dic.keys():
                    dic[node] += 1
                else:
                    dic[node] = 1
                    dic[node.left] = 1 if node.left
                    dic[node.right] = 1 if node.right
            nxt = [(node.left, node.right) for node in level]
            level = [nd for nodeLR in nxt for nd in nodeLR if nd]

        h = max([h for h in dic.values()])
        print(h)
        return h

        
    def levelOrderBottom(self, root):
        queue, res = collections.deque([(root, 0)]), []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) < level+1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        return res
