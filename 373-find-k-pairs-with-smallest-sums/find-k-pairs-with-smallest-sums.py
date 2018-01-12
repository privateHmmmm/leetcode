# -*- coding:utf-8 -*-


#
# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k. 
#
#
# Define a pair (u,v) which consists of one element from the first array and one element from the second array.
#
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
#
#
# Example 1:
#
# Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3
#
# Return: [1,2],[1,4],[1,6]
#
# The first 3 pairs are returned from the sequence:
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
#
#
#
# Example 2:
#
# Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2
#
# Return: [1,1],[1,1]
#
# The first 2 pairs are returned from the sequence:
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
#
#
#
# Example 3:
#
# Given nums1 = [1,2], nums2 = [3],  k = 3 
#
# Return: [1,3],[2,3]
#
# All possible pairs are returned from the sequence:
# [1,3],[2,3]
#
#
#
# Credits:Special thanks to @elmirap and @StefanPochmann for adding this problem and creating all test cases.


import Queue
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        """
        q = Queue.PriorityQueue()
        
        for i1 in range(0, min(k, len(nums1))):
            for i2 in range(0, min(k, len(nums2))):
                q.put([nums1[i1]+nums2[i2], [nums1[i1], nums2[i2]]])
        
        resList = []
        for i in range(0, k):
            if q.qsize() > 0:
                # e=q.get()
                resList.append(q.get()[1])
            else:
                break
        return resList
        """
        
        if not nums1 or not nums2 or not k:
            return []
        
        q=Queue.PriorityQueue()
        
        for i in range(0, min(k, len(nums1))):
            q.put([nums1[i]+nums2[0],0])

        resList = []
        for i in range(0, k):
            if q.qsize() > 0:
                one = q.get()
                resList.append([one[0]-nums2[one[1]], nums2[one[1]]])
                if one[1]<len(nums2)-1:
                    q.put([one[0] - nums2[one[1]] + nums2[one[1]+1], one[1]+1])
            else:
                break
                
        return resList
            
