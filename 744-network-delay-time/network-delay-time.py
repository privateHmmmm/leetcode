# -*- coding:utf-8 -*-


#
# There are N network nodes, labelled 1 to N.
#
# Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
#
# Now, we send a signal from a certain node K.  How long will it take for all nodes to receive the signal?  If it is impossible, return -1.
#
#
# Note:
#
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.
#
#


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        
        graph = collections.defaultdict(list)
        _map = {}
        
        for u, v, t in times:
            graph[u].append([v, t])

        hq = [(0, K)]
        while hq:
            dist, node = heapq.heappop(hq)
            if node in _map: continue
            _map[node] = dist
            for nei, nei_dist in graph[node]:
                if nei not in _map:
                    heapq.heappush(hq, (dist + nei_dist, nei))

        return max(_map.values()) if len(_map) == N else -1
                
