# -*- coding:utf-8 -*-


#
# Given a 2D board and a word, find if the word exists in the grid.
#
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
#
#
# For example,
# Given board = 
#
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
#
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
#


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        n = len(board)
        if n == 0: return False
        m = len(board[0])
        if m == 0: return False
        
        use = [[True for j in range(0, m)] for i in range(0, n)]
        
        def visit(i, j, step):
            
            if step == len(word):return True

            use[i][j] = False
            
            for s in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newI = i + s[0]
                newJ = j + s[1]
                if 0<=newI<n and 0<=newJ<m and use[newI][newJ]==True and board[newI][newJ] == word[step]:
                    if visit(newI, newJ, step+1):
                        return True
                    
            use[i][j] = True
            return False
        
        for i in range(0, n):
            for j in range(0, m):
                if word[0] == board[i][j]:
                    if visit(i, j, 1) == True: return True
        
        return False
