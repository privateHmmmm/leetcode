# -*- coding:utf-8 -*-


#
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
#
# Each element in the array represents your maximum jump length at that position. 
#
#
# Determine if you are able to reach the last index.
#
#
#
# For example:
# A = [2,3,1,1,4], return true.
#
#
# A = [3,2,1,0,4], return false.
#


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        def jump_once(nums, indexes, unable_indexes):
            
            if 0 in indexes:
                return True
                
            print 'enter: ', indexes
            for index in indexes:
                i = index
                tmp_indexes = []
                while i  > 0:
                    if nums[index-i] >= i and (index -i) not in unable_indexes:
                        tmp_indexes.append(index - i)
                        if index == i:
                            return True
                    i = i - 1
                if tmp_indexes != []:
                    ret = jump_once(nums, tmp_indexes, unable_indexes)
                    if ret == True:
                        return True
                        
            unable_indexes.extend(indexes)
            return False
           
        unable_indexes = []     
        return jump_once(nums, [len(nums)-1], unable_indexes)
        """
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True
    
