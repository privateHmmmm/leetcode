# -*- coding:utf-8 -*-


#
# On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves.  The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).
#
#
#
# A chess knight has 8 possible moves it can make, as illustrated below.  Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
#
#
#
#
#
# Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.
#
#
#
# The knight continues moving until it has made exactly K moves or has moved off the chessboard.  Return the probability that the knight remains on the board after it has stopped moving.
#
#
# Example:
#
# Input: 3, 2, 0, 0
# Output: 0.0625
# Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
# From each of those positions, there are also two moves that will keep the knight on the board.
# The total probability the knight stays on the board is 0.0625.
#
#
#
# Note:
# N will be between 1 and 25.
# K will be between 0 and 100.
# The knight always initially starts on the board.
#


class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        
        """
        # TLE
        MOVE=[0]
        
        def moves(i, j, k):
            
            if k == 0:
                MOVE[0] +=1
                return
            
            steps = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
            
            for s in steps:
                newI = i+s[0]
                newJ = j+s[1]
                if 0<=newI<N and 0<=newJ<N:
                    moves(newI, newJ, k-1)

        moves(r, c, K)
        return float(MOVE[0])/(8**K) 
        """
        
        steps = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        DP = [[[0 for k in range(0, K+1)] for j in range(0, N)] for i in range(0, N)]
        for i in range(0, N):
            for j in range(0, N):
                DP[i][j][0] = 1.0
        
        for k in range(1, K+1):
            for i in range(0, N):
                for j in range(0, N): 
                    for s in steps:
                        newI = i+s[0]
                        newJ = j+s[1]
                        if 0<=newI<N and 0<=newJ<N:
                            DP[i][j][k] += 0.125*DP[newI][newJ][k-1]

        return DP[r][c][K]
