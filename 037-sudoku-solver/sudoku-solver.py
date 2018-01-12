# -*- coding:utf-8 -*-


# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# Empty cells are indicated by the character '.'.
#
# You may assume that there will be only one unique solution.
#
#
#
# A sudoku puzzle...
#
#
#
#
# ...and its solution numbers marked in red.
#


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        """
        def Valid(i, j, num):
            
            if num in board[i]:
                return False
            
            if num in [board[k][j] for k in range(0, len(board))]:
                return False
            
            startI = (i/3)*3
            startJ= (j/3)*3
            
            for i1 in range(startI, startI+3):
                for j1 in range(startJ, startJ+3):
                    if num == board[i1][j1]:
                        return False
                    
            return True
                
        def helper(i, j):
            
            if j >= 9:
                return helper(i+1, 0)
            elif i >= 9:
                return True
            else:
                if board[i][j] == ".":
                    for k in range(1, 10):
                        if Valid(i, j, str(k)) == True:
                            board[i][j] = str(k)
                            if True == helper(i, j+1):
                                return True
                            else:
                                board[i][j]="."
                    else:
                        return False
                else:
                    return helper(i, j+1)
        
        helper(0, 0)
        """
    
        _lens = len(board)
        
        check_row = [set() for i in range(0, _lens)]
        check_col = [set() for j in range(0, _lens)]
        check_subbox = [set() for i in range(0, _lens)]
        
        for i in range(0, _lens):
            for j in range(0, _lens):
                if board[i][j] != '.':
                    subbox = (i/3)*3+(j/3)
                    # if (board[i][j] in check_row[i]) or (board[i][j] in check_col[j]) or (board[i][j] in check_subbox[subbox]):
                        # return False
                    check_row[i].add(board[i][j])
                    check_col[j].add(board[i][j])
                    check_subbox[subbox].add(board[i][j])

        
        def helper(i, j):
            
            if i >= 9:
                return True
            elif j >= 9:
                return helper(i+1, 0)
            elif board[i][j] != '.':  # do not forget this
                return helper(i, j+1)
            
            subbox = (i/3)*3+(j/3)
            for kk in range(1, 10):
                k = str(kk) 
                if k not in check_row[i] and k not in check_col[j] and k not in check_subbox[subbox]:
                    check_row[i].add(k)
                    check_col[j].add(k)
                    check_subbox[subbox].add(k)
                    board[i][j] = k
                    if True == helper(i, j+1): return True
                    board[i][j] = '.'
                    check_row[i].remove(k)
                    check_col[j].remove(k)
                    check_subbox[subbox].remove(k)
            
            return False
        
        helper(0, 0)
            
