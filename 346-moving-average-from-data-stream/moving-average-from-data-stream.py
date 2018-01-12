# -*- coding:utf-8 -*-


# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
#
# For example,
#
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3
#
#


class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        
        self.queue = []
        self.size = size
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        
        if len(self.queue) == self.size:
            self.sum -= (self.queue.pop(0))
        self.queue.append(val)
        self.sum += val
        return float(self.sum)/len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
