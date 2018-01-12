# -*- coding:utf-8 -*-


#
# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
#
#
#
#
# OJ's undirected graph serialization:
#
#
# Nodes are labeled uniquely.
#
#
# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
#
#
#
#
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
#
#
#
# The graph has a total of three nodes, and therefore contains three parts as separated by #.
#
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
#
#
#
#
# Visually, the graph looks like the following:
#
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/
#
#
#
#


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        
        """
        # DFS
        _map = {}
        def robot(node):
            # DFS
            if not node: return None
            
            if node in _map: return _map[node]
            
            _map[node] = UndirectedGraphNode(node.label)
            new_node = _map[node]
            for n in node.neighbors:
                new_node.neighbors.append(robot(n))
            
            return new_node
        
        return robot(node)
        """
        
        # BFS
        def getAllNodes(node):
            
            if not node: return []
            
            res = set([node])
            stack = [node]
            while stack:
                node = stack.pop()
                for n in node.neighbors:
                    if n not in res:
                        res.add(n)
                        stack.append(n)
            return list(res)
        
        _map = {}
        allNodes = getAllNodes(node)
        for n in allNodes:
            _map[n] = UndirectedGraphNode(n.label)
        
        for n in allNodes:
            for nei in n.neighbors:
                _map[n].neighbors.append(_map[nei])
        
        return _map.get(node)
        
