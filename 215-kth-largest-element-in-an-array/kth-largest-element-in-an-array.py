# -*- coding:utf-8 -*-


# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
#
#
# Note: 
# You may assume k is always valid, 1 &le; k &le; array's length.
#
# Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.


from heapq import *
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        def swap(i, j):
            if i != j:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                
        def partition(p, r, k):
            
            i = p - 1
            for j in range(p, r):
                if nums[j] < nums[r]:
                    i += 1
                    swap(i, j)
            i += 1
            swap(i, r)
            if (r-i+1) == k:
                return nums[i]
            elif (r-i+1) > k:
                return partition(i+1, r, k)
            else:
                return partition(p, i-1, k-(r-i+1))
            
        return partition(0, len(nums)-1, k)
        """
        
        minHeap = []
        
        for i in range(0, len(nums)):
            heappush(minHeap, nums[i])
            if len(minHeap) > k:
                heappop(minHeap)
        
        return heappop(minHeap)
        
