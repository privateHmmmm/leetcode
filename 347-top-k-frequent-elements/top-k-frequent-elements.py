# -*- coding:utf-8 -*-


#
# Given a non-empty array of integers, return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
#
# Note: 
#
# You may assume k is always valid, 1 &le; k &le; number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
#


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        from heapq import *
        counter = collections.Counter(nums)

        # priority queue
        queue = []
        for num, count in counter.items():
            heappush(queue, [-count, num])
            
        res=[]
        for i in range(0, k):
            d=heappop(queue)
            res.append(d[1])
        
        return res

    
        # counter = sorted(counter.items(), key = lambda item: item[1], reverse=True)
        # lists = []
        # for key, value in counter:
        #     lists.append(key)
        #     if len(lists)>=k:
        #         break
        # return lists
        
        
