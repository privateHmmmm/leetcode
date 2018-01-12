# -*- coding:utf-8 -*-


#
# There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.
#
#
#
# Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.
#
#
#
# For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.
#
#
#
# Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.
#
#
#
# If there isn't such day, output -1.
#
#
# Example 1:
#
# Input: 
# flowers: [1,3,2]
# k: 1
# Output: 2
# Explanation: In the second day, the first and the third flower have become blooming.
#
#
#
# Example 2:
#
# Input: 
# flowers: [1,2,3]
# k: 1
# Output: -1
#
#
#
#
# Note:
#
# The given array will be in the range [1, 20000].
#
#


class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        
        # Bucket Sort, or Binary Search Tree(TODO)
        # time: O(1), space: O(n/(k+1))
        _MAX, _MIN = 2**31-1, -2**31
        n = len(flowers)
        k += 1
        bs = n/k + 1  # !!!!
        
        _min = [_MAX]*bs
        _max = [_MIN]*bs
        
        for i in range(0, len(flowers)):
            bucket = flowers[i]/k
           
            if flowers[i] < _min[bucket] and bucket > 0 and flowers[i] - _max[bucket-1] == k:
                return i + 1
            
            if flowers[i] > _max[bucket] and bucket < (bs-1) and _min[bucket+1] - flowers[i] == k:
                return i + 1
            
            _min[bucket] = min(_min[bucket], flowers[i])
            _max[bucket] = max(_max[bucket], flowers[i])
        
        return -1
            
