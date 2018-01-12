# -*- coding:utf-8 -*-


#
# Given a sorted array of integers nums and integer values a, b and c.  Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array. 
#
# The returned array must be in sorted order.
#
# Expected time complexity: O(n)
#
# Example:
#
# nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,
#
# Result: [3, 9, 15, 33]
#
# nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5
#
# Result: [-23, -5, 1, 7]
#
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all test cases.


class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        
    
        def cal(num):
            return a*num*num + b*num + c
        
        res = [0 for i in range(0, len(nums))]
        
        start, end = 0, len(nums)-1
        index = len(nums)-1 if a >= 0 else 0
        while start<=end:
            startNum = cal(nums[start])
            endNum = cal(nums[end])
            if a >= 0:
                if startNum >= endNum:
                    res[index] = startNum
                    start += 1
                else:
                    res[index] = endNum
                    end -= 1
                index -= 1
            else:
                if startNum <= endNum:
                    res[index] = startNum
                    start += 1
                else:
                    res[index] = endNum
                    end -= 1
                index += 1    
            
        return res

