# -*- coding:utf-8 -*-


#
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
#
#
#
# For example:
#
#
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
#
#
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
#
#
#
# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
#


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
        """
        # DFS
        if n == 1 and edges == []: return True
        if len(edges) != n-1: return False
        biEdges = collections.defaultdict(list)
        for i in range(0, len(edges)):
            biEdges[edges[i][0]].append(edges[i][1])
            biEdges[edges[i][1]].append(edges[i][0])
        
        visited = set([edges[0][0]])
        
        def helper(node, parent):

            neighbors = biEdges[node]
            for nei in neighbors:
                if nei == parent: continue 
                if nei in visited: 
                    return False
                visited.add(nei)
                if False == helper(nei, node):
                    return False
            
            return True
        
        return helper(edges[0][0], -1)
        """
    
        # union-find
        if n == 1 and edges == []: return True
        if len(edges) != n-1: return False
        fa = [i for i in range(n)]
        
        def merge(x, y):
            fa_x = getfa(x)
            fa_y = getfa(y)
            if fa_x != fa_y:
                fa[fa_x] = fa_y
                return True
            else:
                return False
        
        def getfa(x):
            if fa[x] != x:
                fa[x] = getfa(fa[x])
            return fa[x]
        
        for i in range(0, len(edges)):
            if False == merge(edges[i][0], edges[i][1]):
                return False
        
        return True
        
