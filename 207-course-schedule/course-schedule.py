# -*- coding:utf-8 -*-


#
# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
#
# For example:
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
#
# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
#
# Note:
#
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
#
#
#
# click to show more hints.
#
# Hints:
#
# This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
# Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
# Topological sort could also be done via BFS.
#
#


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        n = numCourses
        indegree = [0 for i in range(0, n)]
        graph = [[] for j in range(0, n)]
        
        for p in prerequisites:
            indegree[p[0]] += 1 # p[1] ---- p[0]
            graph[p[1]].append(p[0])
        
        queue = []
        for i in range(0, n):
            if indegree[i] == 0:
                queue.append(i)
        
        cnt = 0
        while queue:
            node = queue.pop(0)
            cnt +=1
            for nei in graph[node]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    queue.append(nei)
        return cnt == n

