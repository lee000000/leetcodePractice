'''
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start'

in the diagram below).

The robot can only move either down or right at any point in time. The robot

is trying to reach the bottom-right corner of the grid (marked 'Finish'

in the diagram below).

How many possible unique paths are there?

start [] [] [] [] [] []
[]    [] [] [] [] [] []
[]    [] [] [] [] [] finish

Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1



        for i in range(m):
            for j in range(n):
                # print((i, j))
                # #print((dp[i-1][j],  dp[i][j - 1]))
                # print((dp[i][j],  dp[i-1][j], dp[i][j - 1]))

                if i == 0:

                    dp[i][j] += dp[i][j - 1]
                elif j == 0:
                    dp[i][j] += dp[i - 1][j]
                else:
                    dp[i][j] += dp[i - 1][j] + dp[i][j - 1]

        # for line in dp:
        #     print(line)
        return dp[m - 1][n - 1]
        # Wrong!
        # Counting of row and column is incorrect
        # if m == 0 or n == 0:
        #     return 0
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        # dp[0][0] = 1
        #
        # # dp[0][1] = dp[1][0] = 1
        # for i in range(0, m):
        #     for j in range(1, n):
        #         # print((i, j))
        #         #print((dp[i-1][j],  dp[i][j - 1]))
        #         dp[i][j] = dp[i-1][j] + dp[i][j - 1]
        #
        #     # print(dp[i])
        # return dp[m - 1][n - 1]


def test():
    sol = Solution()
    print(sol.uniquePaths(3, 7))


if __name__ == "__main__":
    test()
