# -*- coding:utf-8 -*-


#
# Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
#
#
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
#


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        
        start = lower
        res = []
        
        for num in nums:
            if num == start:
                start += 1
            elif start < num:
                if num == start +1:
                    res.append(str(start))
                else:
                    res.append("%d->%d" %(start, num-1))
            start = num + 1
        
        if start == upper:
            res.append(str(start))
        elif start < upper:
            res.append('%d->%d' %(start, upper))
        
        return res
                
