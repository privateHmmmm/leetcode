# -*- coding:utf-8 -*-


#
# Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.
#
#
#
# Example 1:
#
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).Although we have two 1s in the input, we should only return the number of unique pairs.
#
#
#
# Example 2:
#
# Input:[1, 2, 3, 4, 5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
#
#
#
# Example 3:
#
# Input: [1, 3, 1, 5, 4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).
#
#
#
# Note:
#
# The pairs (i, j) and (j, i) count as the same pair.
# The length of the array won't exceed 10,000.
# All the integers in the given input belong to the range: [-1e7, 1e7].
#
#


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        """
        if k < 0:
            return 0
        elif k == 0:
            total=0
            dicts={}
            for num in nums:
                if num in dicts:
                    if dicts[num]==1:
                        total+=1
                        dicts[num]=-1
                else:
                    dicts[num]=1
            return total
                    
            
        
        dict_p = {}
        dict_n = {}
        total = 0
        flag1=True
        flag2=True

        for i in range(0, len(nums)):
            flag1=True
            flag2=True
            if nums[i] in dict_p:
                # find one that is k bigger than self
                total+=1
                del dict_p[nums[i]]
                flag2=False

            if nums[i] in dict_n:
                # find one tha is k smaller than self
                total +=1
                del dict_n[nums[i]]
                flag1=False

            if flag2==True:
                key = nums[i] - k
                dict_n[key]=i
            if flag1==True:
                key = nums[i] + k
                dict_p[key] = i

        return total
        """
        if k>0:
            return len(set(nums)&set(n+k for n in nums))
        elif k==0:
            return sum(v>1 for v in collections.Counter(nums).values())
        else:
            return 0
        
            
                
        
