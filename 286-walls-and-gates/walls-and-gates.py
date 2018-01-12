# -*- coding:utf-8 -*-


#
# You are given a m x n 2D grid initialized with these three possible values.
#
#
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
#
#
#
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
#
#
# For example, given the 2D grid:
#
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
#
#
#
# After running your function, the 2D grid should be:
#
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4
#


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        
        m = len(rooms)
        if m == 0: return 
        n = len(rooms[0])
        if n == 0: return 
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        """
        def DFS(i, j, step):
            
            for d in directions:
                newI = i + d[0]
                newJ = j + d[1]
                if 0<=newI<m and 0<=newJ<n and rooms[newI][newJ] > step:
                    rooms[newI][newJ] = step
                    DFS(newI, newJ, step+1)
        
        for i in range(0, m):
            for j in range(0, n):
                if rooms[i][j] == 0:
                    DFS(i, j, 1)
        """
        
        # BFS
        queue = []
        for i in range(0, m):
            for j in range(0, n):
                if rooms[i][j] == 0:
                    queue.append([i, j])
        
        step = 0
        while queue:
            lens = len(queue)
            k = 0
            step += 1
            while k < lens:
                i, j = queue.pop(0)
                for d in directions:
                    newI = i + d[0]
                    newJ = j + d[1]
                    if 0<=newI<m and 0<=newJ<n and rooms[newI][newJ] > step:
                        rooms[newI][newJ] = step
                        queue.append([newI,newJ])
                k +=1
                    
                    
