# -*- coding:utf-8 -*-


# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
#
# For example, given nums = [-2, 0, 1, 3], and target = 2.
#
# Return 2. Because there are two triplets which sums are less than 2:
#
# [-2, 0, 1]
# [-2, 0, 3]
#
#
# Follow up:
# Could you solve it in O(n2) runtime?
#


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if len(nums) < 3: return 0
        
        nums.sort()
        self.res = 0
        for i in range(0, len(nums)):
            L, R = i+1, len(nums)-1
            while L<R:
                _sum = nums[i] + nums[L] + nums[R]
                if _sum < target:
                    self.res += (R-L)
                    L += 1
                else:
                    R -= 1
        
        return self.res
                    
