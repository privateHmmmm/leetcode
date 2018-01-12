# -*- coding:utf-8 -*-


# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Now your job is to find the total Hamming distance between all pairs of the given numbers.
#
#
# Example:
#
# Input: 4, 14, 2
#
# Output: 6
#
# Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
# showing the four bits relevant in this case). So the answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
#
#
#
# Note:
#
# Elements of the given array are in the range of 0  to 10^9
# Length of the array will not exceed 10^4. 
#
#


class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        distance = 0
        for j in range(0, 32):
            if nums.count(0) == len(nums):
                break

            count1 = 0
            for i in range(0, len(nums)):
                count1 += ((nums[i]>>j) & 1)
                # nums[i] = nums[i] >> 1
            count0 = len(nums) - count1

            distance += count0 * count1

        return distance
            
        """
        numssortedbybit = zip(*map('{:032b}'.format, nums))

        res = 0
        for bit in numssortedbybit:
            res += bit.count('0') * bit.count('1')

        return res
        """    
            
