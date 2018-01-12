# -*- coding:utf-8 -*-


#
# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# Example 1:
#
# Input: [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
#
#
#
# Example 2:
#
# Input: [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
#
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        lists=[]
        new_start=True
        for i in range(0, len(nums)):
            if i == 0:
                lists.append("%d" %nums[0])
            elif nums[i]-nums[i-1]==1:
                new_start=False
                continue
            else:
                if new_start == False:
                    lists[-1] +="->%d" %nums[i-1]
                    
                lists.append("%d" %nums[i])
                new_start=True
                
        if new_start == False:
            lists[-1] +="->%d" %nums[-1]
            
        return lists
    
    
    
                
