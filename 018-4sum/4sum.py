# -*- coding:utf-8 -*-


# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note: The solution set must not contain duplicate quadruplets.
#
#
#
# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
#


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def twoSum(nums, target):

            # remember the nums are sorted. So the binary search is the most fast

            lo = 0
            hi = len(nums) - 1
            lists = []

            while lo < hi:
                if lo > 0 and nums[lo] == nums[lo - 1]:
                    lo += 1
                    continue

                if (nums[lo] + nums[lo+1] > target): break
                if (nums[hi-1] + nums[hi] < target): break
                    
                tmp = nums[lo] + nums[hi]
                if tmp == target:
                    lists.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                elif tmp < target:
                    lo += 1
                else:
                    hi -= 1

            return lists

        def threeSum(nums, target):

            resList=[]
            for i in range(0, len(nums)-2):
                if i >0 and nums[i] == nums[i-1]:
                    continue

                if (nums[i] + nums[i + 1] + nums[i + 2] > target): break
                if (nums[i] + nums[len(nums) - 2] + nums[len(nums) - 1] < target): continue

                lists=twoSum(nums[i + 1:], target - nums[i])
                for l in lists:
                    l.append(nums[i])
                    resList.append(l)

            return resList

        nums.sort()
        resList = []
        for i in range(0, len(nums)-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if (nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target): break
            if (nums[i] + nums[len(nums) - 3] + nums[len(nums) - 2] + nums[len(nums) - 1] < target): continue

            lists = threeSum(nums[i + 1:], target - nums[i])
            for l in lists:
                l.append(nums[i])
                resList.append(l)

        return resList

