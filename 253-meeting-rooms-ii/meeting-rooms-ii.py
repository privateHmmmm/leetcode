# -*- coding:utf-8 -*-


# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
#
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.
#


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        
        starts = []
        ends = []
        for i in range(0, len(intervals)):
            starts.append(intervals[i].start)
            ends.append(intervals[i].end)
        
        starts.sort()
        ends.sort()
        
        res = 0
        end = 0
        for i in range(0, len(intervals)):
            if starts[i] < ends[end]:
                res += 1
            else:
                end += 1
        
        return res
