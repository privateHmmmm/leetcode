# -*- coding:utf-8 -*-


# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.
# For example, the numbers "69", "88", and "818" are all strobogrammatic.


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        _map = {'6': '9', '9': '6', '0': '0', '8': '8', '1': '1'}
        
        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] not in _map or _map[num[left]] != num[right]:
                return False
            left +=1
            right -=1
        
        return True
