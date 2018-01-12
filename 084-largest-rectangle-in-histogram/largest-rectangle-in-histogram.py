# -*- coding:utf-8 -*-


#
# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
#
#
#
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
#
#
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
#
#
# For example,
# Given heights = [2,1,5,6,2,3],
# return 10.
#


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        # 升序，存储
        # 小于，计算
        
        # stack 1 4 5 
        # 2 1 5 6 2 3 0
        # 2: push
        # 1: height = 2, start = -1, max = 2*1 = 2
        # 5: push
        # 6: push
        # 2: height = 6, start = 2, max = 6*1 = 6
        #    height = 5, start = 1, max = 5*2 = 10
        # 3: push
        # 0: height = 3 * 1 = 3
        #    height = 2 * 4 = 8
        
        _max = 0
        stack = []
        heights.append(0)
        for i in range(0, len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                start = -1 if not stack else stack[-1]
                _max = max(_max, height * (i - start - 1))
            stack.append(i)
        
        return _max
