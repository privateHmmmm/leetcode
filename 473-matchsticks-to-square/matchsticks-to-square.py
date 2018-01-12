# -*- coding:utf-8 -*-


# Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
#
#  Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.
#
# Example 1:
#
# Input: [1,1,2,2,2]
# Output: true
#
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
#
#
#
# Example 2:
#
# Input: [3,3,3,3,4]
# Output: false
#
# Explanation: You cannot find a way to form a square with all the matchsticks.
#
#
#
# Note:
#
# The length sum of the given matchsticks is in the range of 0 to 10^9.
# The length of the given matchstick array will not exceed 15.
#
#


class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if not nums:
            return False
        
        if sum(nums) % 4 != 0:
            return False
        
        length=sum(nums)/4
        if max(nums) > length:
            return False
        
        nums.sort(reverse=True)
        
        def DFS(nums, Sum):
            
            if Sum == 0:
                if nums == []:
                    return True
                else:
                    Sum=length
        
            for i in range(0, len(nums)):
                if nums[i] <= Sum:
                    tmp=nums[i]
                    nums.remove(nums[i])
                    if True == DFS(nums, Sum-tmp):
                        return True
                    nums.insert(i, tmp)
                else:
                    break   # TLE first, then sort the array, and break here, I got an accept!!
                
            return False
                
        return DFS(nums, length)
