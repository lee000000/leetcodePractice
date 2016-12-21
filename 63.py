'''
63. Unique Paths II

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique

paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        # Runtime: 52ms
        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 1:
            if not 1 in obstacleGrid[0]:
                return 1
            else:
                return 0
        if n == 1:
            if not [1] in obstacleGrid:
                return 1
            else:
                return 0

        dp = [[0 for _ in range(n)] for _ in range(m)]

        # for k in range(m):
        #     for l in range(n):
        #         if obstacleGrid[k][l] == 1:
        #             dp[k][l] = -1


        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == 0 and j != 0:

                        dp[i][j] += dp[i][j - 1]
                    elif j == 0 and i != 0:
                        dp[i][j] += dp[i - 1][j]
                    elif i == 0 and j == 0:
                        continue
                    else:
                        dp[i][j] += dp[i - 1][j] + dp[i][j - 1]
            # print(dp[i])

        return dp[m - 1][n - 1]



def test():
    obs = [
      [0,0,0],
      [0,0,0],
      [0,1,0],

    ]
    obt = [[0,0,0,0], [0,0,1,1], [1,0,0,0], [0,0,0, 0],[0,0,0,0]]
    sol = Solution()
    print(sol.uniquePathsWithObstacles(obs))


if __name__ == "__main__":
    test()
