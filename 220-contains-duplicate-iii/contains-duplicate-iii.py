# -*- coding:utf-8 -*-


#
# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
#


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        
        if t < 0: return False
        _map = {}
        bucket_size = t + 1
        
        for i, num in enumerate(nums):
            bucket = num / bucket_size
            if (bucket in _map) or \
                ((bucket-1) in _map and (num - _map[bucket-1] <= t)) or \
                ((bucket+1) in _map and (_map[bucket+1] - num <= t)):
                    return True
            
            _map[bucket] = num
            if i >= k:
                bb = nums[i-k] / bucket_size
                del _map[bb]
            
        return False
                
