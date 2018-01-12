# -*- coding:utf-8 -*-


#
# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
#
# For example,
# If nums = [1,2,2], a solution is:
#
#
#
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
#


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        """
        ans = []
        use = [False for i in range(0, len(nums))]
        
        def robot(idx):
            if idx >= len(nums):
                tmp = []
                for i in range(0, len(use)):
                    if use[i] == True:
                        tmp.append(nums[i])
                ans.append(tmp)
                return
            
            if idx>0 and nums[idx-1] == nums[idx] and use[idx-1] == False:
                use[idx] = False
                robot(idx+1)
            else:
                use[idx] = True
                robot(idx+1)
                use[idx] = False
                robot(idx+1)
        
        nums.sort()
        robot(0)
        return ans
        """
        
        ans = []
        def robot(idx, lists):
            
            ans.append(copy.copy(lists))  # !!!
            
            # if idx >= len(nums):
            #     return
            
            for i in range(idx, len(nums)):
                if i != idx and nums[i] == nums[i-1]: 
                    continue
                lists.append(nums[i])
                robot(i+1, lists)
                lists.pop()
        
        nums.sort()
        robot(0, [])
        return ans
                
