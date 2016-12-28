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
    def maximalSquareImproved(self, matrix):
        if len(matrix) == 0:
            return 0

        maxSize = 0
        pre = [0 for _ in range(len(matrix))]
        cur = [0 for _ in range(len(matrix))]
        for i in range(len(matrix)):
            # pre keeps the values of the previously calculated column values
            # starting from column 1
            pre[i] = matrix[i][0]
            maxSize = max(maxSize, pre[i])

        for j in range(1, len(matrix[0])):

            # cur keeps updating the current column value
            cur[0] = matrix[0][j]

            maxSize = max(maxSize, cur[0])
            for i in range(1, len(matrix)):
                if matrix[i][j] == 1:
                    cur[i] = min(cur[i - 1], min(pre[i - 1], pre[i])) + 1
                    maxSize = max(maxSize, cur[i])
            # this swap step rolls the pre to be the current column value

            pre, cur = cur, pre

            # clear out cur array to store new values
            cur = [0 for _ in range(len(cur))]

        return maxSize * maxSize



    # basic DP
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
    matrix = [[1,1,1,1],[1,1,1,0],[1,1,1,0]]
    sol = Solution()
    print(sol.maximalSquareImproved(matrix))


if __name__ =="__main__":
    test()
