# -*- coding:utf-8 -*-


# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
# 11110110101100000000
# Answer: 1
# Example 2:
# 11000110000010000011
# Answer: 3
#
# Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.


class Solution(object):
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        """
        # BFS approach
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        if m == 0: return 0
        ans = 0
        step = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = [-1 for i in range(0, n*m)]
        
        def floodfill(i, j):
            
            h = 0
            queue[0] = [i, j] 
            grid[i][j] = '0'
            r = 1 # [h, r)
        
            while h<r:
                ii, jj = queue[h]
                h +=1
                for s in step:
                    newi = ii + s[0]
                    newj = jj + s[1]
                    if 0<=newi<n and 0<=newj<m and grid[newi][newj] == '1':
                        grid[newi][newj] = '0'
                        queue[r] = [newi, newj]
                        r +=1
        
        for i in range(0, n):
            for j in range(0,m):
                if grid[i][j] == '1':
                    ans +=1
                    floodfill(i, j)
        
        return ans
        """
        
        """
        # union-find 
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        if m == 0: return 0
        
        def merge(x, y):
            fx = getfa(x)
            fy = getfa(y)
            if fx != fy:
                fa[fx] = fy
        
        def getfa(x):
            if fa[x]!=x:
                fa[x]=getfa(fa[x])
            return fa[x]
        
        step = [(1, 0), (0, 1)]
        fa = range(0, n*m)
        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j]=='1':
                    for s in step:
                        newI = i + s[0]
                        newJ = j + s[1]
                        if 0<=newI<n and 0<=newJ<m and grid[newI][newJ]=='1':
                            merge(i*m+j, newI*m+newJ)

        Set = set()
        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == '1':
                    Set.add(getfa(i*m+j))
        
        return len(Set)
        """
        
        # DFS
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0
        steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def DFS(i, j):
            
            grid[i][j] = '0'
            
            for s in steps:
                newI = i + s[0]
                newJ = j + s[1]
                if 0<=newI<m and 0<=newJ<n and grid[newI][newJ] == '1':
                    DFS(newI, newJ)
        
        res = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1':
                    res +=1
                    DFS(i, j)
        
        return res
        
