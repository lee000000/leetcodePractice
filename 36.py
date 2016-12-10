'''
36. Valid Sudoku


Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are

filled with the character '.'.

'''
import collections
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        check = []
        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if (c != "."):
                    check += [(c, i), (j, c), (i/3, j/3, c)]
        if (len(check) != len(set(check))):
            return False
        else:
            return True


if __name__ == "__main__":
    b = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    sol = Solution()
    print(sol.isValidSudoku(b))
