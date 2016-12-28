'''
221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the

largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
'''
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        maxSoFar = 0
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    if matrix[i][j] == 1:
                        print((i, j))
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                maxSoFar = max(maxSoFar, dp[i][j])
                print(maxSoFar)
        print(dp)
        return maxSoFar * maxSoFar


def test():
    matrix = [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
    sol = Solution()
    print(sol.maximalSquare(matrix))


if __name__ =="__main__":
    test()
