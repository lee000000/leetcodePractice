'''
289. Game of Life


According to the Wikipedia's article: "The Game of Life,

also known simply as Life, is a cellular automaton devised by

the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state

live (1) or dead (0). Each cell interacts with its eight neighbors

(horizontal, vertical, diagonal) using the following four rules

(taken from the above Wikipedia article):
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

1. Any live cell with fewer than two live neighbors dies, as if caused

by under-population.

2. Any live cell with two or three live neighbors lives on to the next

generation.

3. Any live cell with more than three live neighbors dies, as if by over-population..

4. Any dead cell with exactly three live neighbors becomes a live cell, as if by

reproduction.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Write a function to compute the next state (after one update) of the board

given its current state.

Follow up:
Could you solve it in-place? Remember that the board needs to be updated

at the same time: You cannot update some cells first and then use their

updated values to update other cells.

In this question, we represent the board using a 2D array. In principle,

the board is infinite, which would cause problems when the active area

encroaches the border of the array. How would you address these problems?
'''
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        ur = 0
        lc = 0
        br = len(board)
        rc = len(board[0])
        s = 0
        while s < br // 2 and s < rc // 2:
            # traverse each layer
            self.changeLayer(board, ur, br, lc, rc)
            ur += 1
            br -= 1
            lc += 1
            rc -= 1
            s += 1

    def changeLayer(self, board, r1, r2, c1, c2):
        i = r1
        j = c1
        # upper row
        while j < c2:
            self.toggleLife(board[i][j])
            j += 1

        # right column
        while i < r2:
            self.toggleLife(board[i][j])
            i += 1

        # Bottom row
        while j >= 0:
            self.toggleLife(board[i][j])
            j -= 1

        while i > 0:
            self.toggleLife(board[i][j])
            i -= 1


    def toggleLife(self, board, i, j):
