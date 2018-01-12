# -*- coding:utf-8 -*-


# Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.
#
#
#     Example 1:
#
#
# Given points = [[1,1],[-1,1]], return true.
#
#
#
#     Example 2:
#
#
# Given points = [[1,1],[-1,-1]], return false.
#
#
# Follow up:
# Could you do better than O(n2)?
#
#
# Credits:Special thanks to @memoryless for adding this problem and creating all test cases.


class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """

        if len(points) <= 1: return True
        
        _set = set()
        _min, _max = 2**31-1, -2**31
        for point in points:
            _min = min(_min, point[0])
            _max = max(_max, point[0])
            _set.add("%d_%d" %(point[0], point[1]))
        
        x_sum = _min+_max
        for point in points:
            p = "%d_%d" %(x_sum-point[0], point[1])
            if p not in _set:
                return False

        return True
            
