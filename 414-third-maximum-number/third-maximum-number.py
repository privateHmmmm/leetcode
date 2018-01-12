# -*- coding:utf-8 -*-


# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
#
# Example 1:
#
# Input: [3, 2, 1]
#
# Output: 1
#
# Explanation: The third maximum is 1.
#
#
#
# Example 2:
#
# Input: [1, 2]
#
# Output: 2
#
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
#
#
#
# Example 3:
#
# Input: [2, 2, 3, 1]
#
# Output: 1
#
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.
#
#


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max1 = -sys.maxsize
        max2 = -sys.maxsize
        max3 = -sys.maxsize
        
        for num in nums:
            if max1 <= num:
                if max1 != num:
                    max3 = max2
                    max2 = max1
                    max1 = num
            elif max2 <= num < max1:
                if num != max2:
                    max3 = max2
                    max2 = num
            elif max3 <= num:
                max3 = num
        
        print max1, max2,max3
        return max3 if max3>-sys.maxsize else max1
                
