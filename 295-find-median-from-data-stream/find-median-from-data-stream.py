# -*- coding:utf-8 -*-


# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
# Examples: 
# [2,3,4] , the median is 3
# [2,3], the median is (2 + 3) / 2 = 2.5 
#
#
# Design a data structure that supports the following two operations:
#
#
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
#
#
#
# For example:
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
#
#
# Credits:Special thanks to @Louis1992 for adding this problem and creating all test cases.


from heapq import *
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.small, self.large = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))
        
    def findMedian(self):
        """
        :rtype: float
        """
        
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
