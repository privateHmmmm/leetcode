# -*- coding:utf-8 -*-


# You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.
#
# Example 1:
#
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3
# 3, 4, 5
#
#
#
# Example 2:
#
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3, 4, 5
# 3, 4, 5
#
#
#
# Example 3:
#
# Input: [1,2,3,4,4,5]
# Output: False
#
#
#
# Note:
#
# The length of the input is in range of [1, 10000]
#
#


class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        
        counter = collections.Counter(nums)
        start = collections.Counter([])
        
        for num in nums:
            
            if counter[num] == 0:
                continue
            elif start[num] > 0:
                start[num] -=1
                start[num+1] +=1
                counter[num] -=1
            elif counter[num+1] > 0 and counter[num+2] > 0:
                counter[num] -= 1
                counter[num+1] -= 1
                counter[num+2] -= 1
                start[num+3] +=1
            else:
                return False
        return True
