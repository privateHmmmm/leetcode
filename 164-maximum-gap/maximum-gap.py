# -*- coding:utf-8 -*-


# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
#
# Try to solve it in linear time/space.
#
# Return 0 if the array contains less than 2 elements.
#
# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
#
# Credits:Special thanks to @porker2008 for adding this problem and creating all test cases.


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 2: return 0
        
        _max = max(nums)
        _min = min(nums)
        slot = len(nums)-1
        size = math.ceil((float(_max)-_min)/slot)
        # bucket: [min, min+size), [min+size, min+2*size), [min, 3*size) ...
        # maybe min and max can not be put into the bucket:
        # [8,9,10,11,16] size=(16-8)/(5-1)=2
        # [8, 10), [10, 12), [12, 14), [14, 16)     
        MIN_VALUE = _min-1
        MAX_VALUE = _max+1
        buckets_min = [MAX_VALUE] * slot
        buckets_max = [MIN_VALUE] * slot
        
        for i in range(0, len(nums)):
            if nums[i] != _min and nums[i] != _max:
                index = int((nums[i]-_min)/size)
                buckets_min[index] = min(nums[i], buckets_min[index])
                buckets_max[index] = max(nums[i], buckets_max[index])
        
        previous = _min
        max_gap = 0
        for i in range(0, slot):
            if MAX_VALUE == buckets_min[i]:
                continue
            max_gap = max(max_gap, buckets_min[i]-previous) 
            previous = buckets_max[i]
        
        max_gap = max(max_gap, _max-previous)
        return max_gap
                
