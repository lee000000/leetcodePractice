'''
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top

left to bottom right which minimizes the sum of all numbers along its path.
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        if len(grid[0]) == 1 or len(grid) == 1:
            return sum(grid)
            
        m = len(grid)
        n = len(grid[0])
        minDP = [[0 for _ in range(n)] for _ in range(m)]

        for line in grid:
            print(line)
        print("#################################")
        minDP[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j != 0:
                    minDP[i][j] = minDP[i][j - 1] + grid[i][j]
                elif j == 0 and i != 0:
                    minDP[i][j] = minDP[i - 1][j] + grid[i][j]
                else:
                    minDP[i][j] = min(minDP[i - 1][j], minDP[i][j - 1]) + grid[i][j]
            print(minDP[i])
        return minDP[m - 1][n - 1]


def test():
    grid = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    sol = Solution()
    print(sol.minPathSum(grid))


if __name__ == "__main__":
    test()
