# -*- coding:utf-8 -*-


# Given an integer array of size n, find all elements that appear more than &lfloor; n/3 &rfloor; times. The algorithm should run in linear time and in O(1) space.


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        count1 = 0
        count2 = 0
        major1 = 0
        major2 = 0

        Min = len(nums) / 3 + 1

        for num in nums:
            if num == major1:
                count1 += 1
            elif num == major2:
                count2 += 1
            elif count1 == 0:
                major1 = num
                count1 = 1
            elif count2 == 0:
                major2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        #print 'count1 %d, major1 %d' %(count1, major1)
        #print 'count2 %d, major2 %d' %(count2, major2)


        return [n for n in set([major1, major2]) if nums.count(n) >= Min]

