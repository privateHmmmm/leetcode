# -*- coding:utf-8 -*-


#
# Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.
#
#
# Example 1:
#
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; The number 2 can't find next greater number; The second 1's next greater number needs to search circularly, which is also 2.
#
#
#
# Note:
# The length of given array won't exceed 10000.
#


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if not nums:
            return []
        
        res=[-1 for i in range(len(nums))]
        i=0
        flag=False
        stack=[]
        
        while 1:
            while stack and nums[stack[-1]] <nums[i]:
                res[stack[-1]]=nums[i]
                stack.pop()
                
            stack.append(i)
            if i>=len(nums)-1:
                if flag==True:
                    break
                else:
                    i=0
                    flag=True
            else:
                i+=1
                
        # for idx in stack:
            # if res[idx]!=-1:
                # res[idx]=-1
        
        return res
    
