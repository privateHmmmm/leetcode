# -*- coding:utf-8 -*-


# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
#
# Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
#
# Example:
#
# Input:
# [[0,0],[1,0],[2,0]]
#
# Output:
# 2
#
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
#
#


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        res = 0
        map = collections.Counter()
        
        for i in range(0, len(points)):
            for j in range(0, len(points)):
                if j == i:
                    continue
                distance = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
                map[distance] +=1
            
            for v in map.values():
                res += v*(v-1)
            
            map.clear()
        
        return res
