# -*- coding:utf-8 -*-


#
# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
#
#
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
#
#
#
#
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
#
#
#
#
# Write a function to compute the next state (after one update) of the board given its current state.
#
#
# Follow up: 
#
# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
#
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        # 2,3  live --> live
        # 1    live --> die (under population)
        # 4    live --> die (over popularity)
        # 3    die --> live (reproduction)
        
        # time: O(m*n)
        # 00   01
        # 10   11
        m = len(board)
        n = len(board[0])
        
        def countLive(i, j):
            
            count = 0
            for ii in range(max(0, i-1), min(m-1, i+1)+1):
                for jj in range(max(0, j-1), min(n-1, j+1)+1):
                    if ii == i and jj == j: continue
                    if (board[ii][jj] & 1) == 1:
                        count +=1
            
            return count
        
        for i in range(0, m):
            for j in range(0, n):
                count = countLive(i, j)
                if (board[i][j] == 1 and count in [2, 3]) or (board[i][j] == 0 and count == 3):
                    board[i][j] += 2
        print board
        
        for i in range(0, m):
            for j in range(0, n):
                board[i][j] >>= 1
        
