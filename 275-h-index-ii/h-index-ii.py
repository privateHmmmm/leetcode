# -*- coding:utf-8 -*-


#
# Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
#


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        # binary search O(logn)
        lo = 0 
        hi = len(citations) - 1
        
        while lo <= hi:
            mid = (lo + hi)/2
            if citations[mid] == len(citations)-mid:
                return len(citations)-mid
            elif citations[mid] > (len(citations) - mid):
                hi = mid - 1
            else:
                lo = mid + 1
        
        return len(citations)-lo
