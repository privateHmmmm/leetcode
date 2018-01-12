# -*- coding:utf-8 -*-


# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.


# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        
        def gcd(a, b):
            if a == 0: return b
            return gcd(b%a, a)
        
        if len(points) < 2: return len(points)
        _max = 0
        
        for i in range(0, len(points)):
            samePoint = 1
            sameXaxis = 1
            _map = collections.Counter()
            tmp_max = 0
            for j in range(0, len(points)):
                if i == j: continue    
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    samePoint +=1
                elif points[i].x == points[j].x:
                    sameXaxis +=1
                else:
                    numerator = points[i].y - points[j].y
                    denominator = points[i].x - points[j].x
                    _gcd = gcd(numerator, denominator)
                    key = '%d/%d' %(numerator/_gcd, denominator/_gcd)
                    _map[key] += 1
                    tmp_max = max(tmp_max, _map[key])
            else:
                tmp_max += samePoint
                # print tmp_map, samePoint, sameXaxis
                tmp_max = max(tmp_max, sameXaxis)
                
            _max = max(_max, tmp_max)
            
        return _max
                    
