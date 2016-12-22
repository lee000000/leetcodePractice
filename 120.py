'''
120. Triangle

Given a triangle, find the minimum path sum from top to bottom.

Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,-1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n

is the total number of rows in the triangle.
'''
import sys
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        minSum = triangle[-1]

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                print(j)
                print(minSum)
                minSum[j] = min(minSum[j], minSum[j + 1]) + triangle[i][j]
        print(minSum)
        return minSum[0]


def test():
    t = [
         [1],
        [2,3],
       [1,2,3]
    ]
    sol = Solution()
    print(sol.minimumTotal(t))

if __name__ == "__main__":
    test()
