# -*- coding:utf-8 -*-


#
#     Given an unsorted array nums, reorder it such that
#     nums[0] < nums[1] > nums[2] < nums[3]....
#
#
#
#     Example:
#     (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
#     (2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].
#
#
#
#     Note:
#     You may assume all input has valid answer.
#
#
#
#     Follow Up:
#     Can you do it in O(n) time and/or in-place with O(1) extra space?
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        
        # [4, 5, 6]  lo=1, hi=2 [5,6,4]
        # [1,2,3,4] lo = 1, hi = 3 [2,4,1,3]
        
        
        copy_nums = sorted(nums)
        n = len(nums)
        hi = n-1
        lo = (n-1)/2
        
        for i in range(0, n):
            if i & 1:
                nums[i] = copy_nums[hi]
                hi -=1
            else:
                nums[i] = copy_nums[lo]
                lo -=1
            
        
            
            
