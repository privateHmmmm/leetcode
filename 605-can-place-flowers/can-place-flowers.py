# -*- coding:utf-8 -*-


# Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
#
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
#
# Example 1:
#
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
#
#
#
# Example 2:
#
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
#
#
#
# Note:
#
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.
#
#


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        """
        if max(flowerbed) == 0:
            return (len(flowerbed)+1)/2 >= n
        
        constantZeroDict = collections.Counter()
        cnt = 0
        left = -1
        right = -1
        for i, isEmpty in enumerate(flowerbed):
            if isEmpty == 1:
                if left == -1: 
                    left = cnt
                else:
                    if cnt > 0: constantZeroDict[cnt] +=1
                cnt = 0
            else:
                cnt +=1
        else:
            if cnt > 0: right = cnt
                
        print left, right, constantZeroDict
        total = 0
        if left > 0: total += left/2
        if right > 0: total += right/2
        
        for Zeronum in constantZeroDict.keys():
            total += ((Zeronum-1)/2)*constantZeroDict[Zeronum]
        return total >=n
        """
        
        initFlower = flowerbed.count(1)
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0:
                if len(flowerbed) == 1 or (i == 0 and flowerbed[i+1]==0) or \
                (i == len(flowerbed)-1 and flowerbed[-2] == 0) or \
                (flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                
        return (flowerbed.count(1)-initFlower) >= n
                      
