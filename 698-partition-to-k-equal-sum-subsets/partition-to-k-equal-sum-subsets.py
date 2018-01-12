# -*- coding:utf-8 -*-


# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
#
# Example 1:
#
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
#
#
#
# Note:
# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.
#


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        # nums.sort(reverse = True)
        _sum = sum(nums)
        if _sum % k != 0:
            return False
        aver = _sum/k
        # visited = [False for i in range(0, len(nums))]
        visited = [2**len(nums)-1]
        _map = {}
        
        def robot(target):
            
            if target == 0 and visited[0] == 0:
                return True
            
            if visited[0] in _map:
                return _map[visited[0]]
        
            if target == 0:
                target = aver
            
            for i in range(0, len(nums)):
                if nums[i]<=target and ((visited[0]>>i)&1) > 0:
                    # visited[i] = True
                    visited[0] ^= (1<<i)
                    if True == robot(target-nums[i]):
                        _map[visited[0]] = True 
                        return True
                    # visited[i] = False
                    visited[0] |= (1<<i)
                    
            _map[visited[0]] = False
            return False
        
        return robot(aver)
        
