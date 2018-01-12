# -*- coding:utf-8 -*-


# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list. 
#
# Example 1:
#
# Input: ["23:59","00:00"]
# Output: 1
#
#
#
# Note:
#
# The number of time points in the given list is at least 2 and won't exceed 20000.
# The input time is legal and ranges from 00:00 to 23:59.
#
#


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        
        if len(timePoints) >= 1440:
            return 0
        
        timePoints.sort()
        Min = 1440
        lens = len(timePoints)
        
        for i in range(0, lens):
            
            tmp = 60*(int(timePoints[(i+1)%lens][0:2])-int(timePoints[i][0:2])) + \
                (int(timePoints[(i+1)%lens][3:])-int(timePoints[i][3:]))
        
            if i < lens-1:
                Min = min(Min, tmp)
            else:
                Min = min(Min, 1440+tmp)
        return Min
