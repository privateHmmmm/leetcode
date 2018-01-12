# -*- coding:utf-8 -*-


#
# Equations are given in the format A / B = k, where  A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.
#
# Example:
# Given  a / b = 2.0, b / c = 3.0. queries are:  a / c = ?,  b / a = ?, a / e = ?,  a / a = ?, x / x = ? . return  [6.0, 0.5, -1.0, 1.0, -1.0 ].
#
#
# The input is:  vector&lt;pair&lt;string, string&gt;&gt; equations, vector&lt;double&gt;&amp; values, vector&lt;pair&lt;string, string&gt;&gt; queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return  vector&lt;double&gt;.
#
#
# According to the example above:
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
#
#
#
# The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
#


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        """
        fa = []
        value = []
        _map = {}
        
        def merge(x, y, w):
            fx = getfa(x)
            fy = getfa(y)
            if fy != fx:
                # x/fx=value[x]; y/fy=value[y];x/y=w; so fx/fy= (y/fy)*(x/y)/(x/fx) !!!
                fa[fx] = fy
                value[fx]=value[y]*w/(value[x])
                
            return
        
        def getfa(x):
            if fa[x] != x:
                newfa = getfa(fa[x])
                value[x] *= value[fa[x]]
                fa[x] = newfa
            return fa[x]
        
        for i in range(0, len(equations)):
            for k in range(0, 2):
                if equations[i][k] not in _map:
                    _map[equations[i][k]]=len(fa)
                    fa.append(len(fa))
                    value.append(1.0)

            merge(_map[equations[i][0]], _map[equations[i][1]], values[i])
        
        ans=[]
        for i in range(0, len(queries)):
            if queries[i][0] not in _map or queries[i][1] not in _map:
                ans.append(-1.0)
            else:
                x = _map[queries[i][0]]
                y = _map[queries[i][1]]
                if getfa(x) != getfa(y):
                    ans.append(-1.0)
                else:
                    ans.append(value[x]/value[y])
        
        return ans
        """
        
        def DFS(start, end, value, visited):
            
            if start not in _map: return -1.0
            if start in visited: return -1.0
            
            if start == end: return value
            
            visited.add(start)
            for i in range(0, len(_map[start])):
                _next = _map[start][i][0]
                _val = _map[start][i][1]
                sub = DFS(_next, end, value*_val, visited)
                if sub != -1.0: return sub
            visited.remove(start)
            return -1.0
        
        _map = collections.defaultdict(list)
        res = []
        
        for i in range(0, len(equations)):
            _map[equations[i][0]].append([equations[i][1], values[i]])
            _map[equations[i][1]].append([equations[i][0], 1.0/values[i]])
            
        for i in range(0, len(queries)):
            res.append(DFS(queries[i][0], queries[i][1], 1.0, set()))

        return res
