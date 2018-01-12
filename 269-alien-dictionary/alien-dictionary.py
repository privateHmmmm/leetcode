# -*- coding:utf-8 -*-


#
# There is a new alien language which uses the latin alphabet. 
# However, the order among letters are unknown to you. 
# You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language.
# Derive the order of letters in this language.
#
#
#
# Example 1:
# Given the following words in dictionary,
#
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
#
#
#
# The correct order is: "wertf".
#
#
# Example 2:
# Given the following words in dictionary,
#
# [
#   "z",
#   "x"
# ]
#
#
#
# The correct order is: "zx".
#
#
# Example 3:
# Given the following words in dictionary,
#
# [
#   "z",
#   "x",
#   "z"
# ]
#
#
#
# The order is invalid, so return "".
#
# Note:
#
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.
#
#


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        # 拓扑排序（topological-sort）   graph --> indegree = 0 --> BFS
        _map = collections.defaultdict(set)
        indegree = collections.Counter()
        
        # count all node count
        count = 0
        for word in words:
            for c in word:
                if indegree[c] == 0:
                    indegree[c] = 1
                    count += 1
        
        # initialize indegree, build graph
        for i in range(0, len(words)-1):
            cur = words[i]
            _next = words[i+1]
            lens = min(len(cur), len(_next))
            for j in range(0, lens):
                if cur[j] != _next[j]:
                    if _next[j] not in _map[cur[j]]: # !!!
                        _map[cur[j]].add(_next[j])
                        indegree[_next[j]] += 1
                    break  # !!!
                    
        queue = []
        for k, v in indegree.iteritems():
            if v == 1:
                queue.append(k)
                
        res = ""
        while queue:
            c = queue.pop(0)
            res += c
            if c in _map:
                for nei in _map[c]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        queue.append(nei)
        
        # print _map, res
        if len(res) == count: return res
        return ""
        
