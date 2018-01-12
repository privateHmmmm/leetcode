# -*- coding:utf-8 -*-


#
# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        dicts={}
        for num in nums:
            if num in dicts:
                return True
            else:
                dicts[num]=1
        
        return False
