# -*- coding:utf-8 -*-


# Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B. 
#
# Example 1:
#
# Input:
# nums = [1,3,1]
# k = 1
# Output: 0 
# Explanation:
# Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
#
#
#
# Note:
#
# 2 <= len(nums) <= 10000.
# 0 <= nums[i] < 1000000.
# 1 <= k <= len(nums) * (len(nums) - 1) / 2.
#
#


class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # find the smallest distance m, such that at least k pairs have distance <= m
        # 先排序，再二分法查找差值数量，最关键的是用了dp去简化每次查找的时间到O(n)
        # binary search + DP
        
        # time: O(nlog(max(n, # of num)) = O(nlog(n^2)) = O(2nlog(n))
        
        nums.sort()
        def getPairNum(m):
            
            # time: O(n)  DP
            cnt = 0
            j = 0
            for i in range(0, len(nums)):
                while j < len(nums) and (nums[j]-nums[i] <= m):
                    j += 1
                cnt += (j-i-1)
            
            return cnt
        
        l, r = 0, nums[-1]-nums[0]
        while l <= r:
            m = (r-l)/2+l
            pairs = getPairNum(m)
            if pairs < k:
                l = m + 1
            else:
                r = m - 1
        
        return l
            
