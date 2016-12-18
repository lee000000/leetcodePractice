'''
70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct

ways can you climb to the top?
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1. naive recursive, TLE
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


        # 2. Improved DP
        if n <= 0:
            return 0
        if n == 1:
            return 1
        # pre, cur = 1, 2
        dp = [1, 2]
        i = 2
        while i < n:
            dp.append(dp[-1] + dp[-2])
            i += 1
        return dp[-1]

        # 3. no dp list, space complexity O(1)
        # best runtime among three
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        pre = 1
        cur = 2
        for i in range(3, n):
            # dp.append(dp[-1] + dp[-2])
            pre, cur = cur, pre + cur

        return pre + cur
