# -*- coding:utf-8 -*-


# We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
#
# Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.
#
# Example 1:
#
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
#
#
#
# Note:
# The length of the input array will not exceed 20,000.
#
#
#


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dicts = collections.Counter(nums)
        Max = 0
        for k in dicts.keys():
            if k+1 in dicts:
                Max = max(Max, dicts[k] + dicts[k+1])
        
        
        # nums = dicts.keys()
        
        
        
        # for k, v in dicts.iteriterms():
        
        # nums.sort()
        # Max = 0
        # for i in range(0, len(nums)):
            
            
            # if i > 0 and nums[i] - nums[i-1] == 1:
                # Max = max(Max, dicts[nums[i]] + dicts[nums[i-1]])
        
        return Max
