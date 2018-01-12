# -*- coding:utf-8 -*-


# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
#
#
# A partially filled sudoku which is valid.
#
#
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
#


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        _lens = len(board)
        
        check_row = [set() for i in range(0, _lens)]
        check_col = [set() for j in range(0, _lens)]
        check_subbox = [set() for i in range(0, _lens)]
        
        for i in range(0, _lens):
            for j in range(0, _lens):
                if board[i][j] != '.':
                    subbox = (i/3)*3+(j/3)
                    if (board[i][j] in check_row[i]) or (board[i][j] in check_col[j]) or (board[i][j] in check_subbox[subbox]):
                        return False
                    check_row[i].add(board[i][j])
                    check_col[j].add(board[i][j])
                    check_subbox[subbox].add(board[i][j])
        
        return True
                    
