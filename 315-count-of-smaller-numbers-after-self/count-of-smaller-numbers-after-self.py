# -*- coding:utf-8 -*-


#
# You are given an integer array nums and you have to return a new counts array.
# The counts array has the property where counts[i] is 
# the number of smaller elements to the right of nums[i].
#
#
# Example:
#
#
# Given nums = [5, 2, 6, 1]
#
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#
#
#
# Return the array [2, 1, 1, 0].
#


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = [0 for i in range(0, len(nums))]
        pair = []
        for i in range(0, len(nums)):
            pair.append([nums[i], i]) # record nums original index
        
        def merge(p, mid, r):
            
            tmp1 = copy.copy(pair[p:mid+1])
            tmp2 = copy.copy(pair[mid+1:r+1])
            p1 = 0; p2 = 0; p3 = p
            while p1 < len(tmp1) or p2 < len(tmp2):
                if p1<len(tmp1) and ((p2 < len(tmp2) and tmp1[p1][0] <= tmp2[p2][0]) 
                                or (p2 == len(tmp2))):
                    res[tmp1[p1][1]] += p2
                    pair[p3] = tmp1[p1]
                    p1 +=1
                else:
                    # res[tmp1[p1][1]] += (p2 + 1)  !!!!!
                    pair[p3] = tmp2[p2]
                    p2 +=1
                p3 +=1
         
        
        def mergeSort(p, r):
            
            if r <= p: return
            
            mid = (p+r)/2
            mergeSort(p, mid)
            mergeSort(mid+1, r)
            merge(p, mid, r)
         
        mergeSort(0, len(nums)-1)
        return res                    
                            
