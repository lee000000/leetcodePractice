'''
463. Island Perimeter

You are given a map in form of a two-dimensional integer grid

where 1 represents land and 0 represents water. Grid cells are

connected horizontally/vertically (not diagonally). The grid is

completely surrounded by water, and there is exactly one island

(i.e., one or more connected land cells). The island doesn't have

"lakes" (water inside that isn't connected to the water around the

island). One cell is a square with side length 1. The grid is

rectangular, width and height don't exceed 100. Determine the

perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes

in the image below:
https://leetcode.com/problems/island-perimeter/
'''
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dic = {}
        p = 0
        # Parse row by row
        row = 0
        for r in grid:
            # in one row, parse column by column
            col = 0
            for c in r:
                if c == 1:
                    # count border
                    if (row == 0):
                        p += 1
                    if (row == len(grid) - 1):
                        p += 1
                    if (col == 0):
                        p += 1
                    if (col == len(grid[0]) - 1):
                        p += 1
                    # count 0s surrounding c
                    if (col != 0 and grid[row][col - 1] == 0):
                        p += 1
                    if (col != len(grid[0]) - 1 and grid[row][col+1] == 0):
                        p += 1
                    if (row != 0 and grid[row - 1][col] == 0):
                        p += 1
                    if (row != len(grid) - 1 and grid[row + 1][col] == 0):
                        p += 1
                    print(p)
                col += 1
            row += 1
        return p


if __name__ == "__main__":
    a = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
    sol = Solution()
    print(sol.islandPerimeter(a))
