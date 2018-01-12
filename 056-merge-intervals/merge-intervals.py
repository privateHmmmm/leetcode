# -*- coding:utf-8 -*-


# Given a collection of intervals, merge all overlapping intervals.
#
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
#


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        """
        1)
        |_______|               |_______|
            |_________|    or      |__|
         
        2)
        |_______|
                   |________|
        
        """
        
        if len(intervals) <= 1: return intervals
        
        intervals.sort(key=lambda x: x.start)
        res = []
        start = intervals[0].start
        end = intervals[0].end
        
        for inv in intervals[1:]:
            if inv.start > end:
                res.append(Interval(start, end))
                start = inv.start
                end = inv.end
            else:
                end = max(end, inv.end)
        
        res.append(Interval(start, end))
        return res
            
        
