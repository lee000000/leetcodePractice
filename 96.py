'''
96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees)

that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        1. subproblems
            - for i <= n, what is total number of possible unique trees with i number
            of nodes
            - there are n subproblems
        2. guessing solution for subproblem assuming something already known
            - For a particular root at i, there are
                F(i, n) = G(i - 1) * G(n - i) unique roots where G(n) is the number
                of unique trees for a sequence of length (k)
        3. recurrences
            - G(n) = F(0, n) + F(1, n) + ...+F(n - 1, n)
                   = G(0) * G(n - 1) + G(1) * G(n - 2) + ... + G(n - 1) * G(1)
        4. recurrence and memoization
            - time O(n*n)
        5.

        runtime 35 ms
        """
        if n == 0:
            return 1
        dpCount = [0] * (n + 1)
        dpCount[0] = 1
        dpCount[1] = 1
        for i in range(2, n + 1):
            for j in range(i + 1):
                dpCount[i] += dpCount[j - 1] * dpCount[i - j]
        return dpCount[n]
