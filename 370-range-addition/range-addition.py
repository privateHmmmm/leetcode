# -*- coding:utf-8 -*-


# Assume you have an array of length n initialized with all 0's and are given k update operations.
#
# Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.
#
# Return the modified array after all k operations were executed.
#
# Example:
#
# Given:
#
#     length = 5,
#     updates = [
#         [1,  3,  2],
#         [2,  4,  3],
#         [0,  2, -2]
#     ]
#
# Output:
#
#     [-2, 0, 3, 5, 3]
#
#
#
# Explanation:
#
# Initial state:
# [ 0, 0, 0, 0, 0 ]
#
# After applying operation [1, 3, 2]:
# [ 0, 2, 2, 2, 0 ]
#
# After applying operation [2, 4, 3]:
# [ 0, 2, 5, 5, 3 ]
#
# After applying operation [0, 2, -2]:
# [-2, 0, 3, 5, 3 ]
#
#
#
# Credits:Special thanks to @vinod23 for adding this problem and creating all test cases.


class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        
        # time: O(n+k) space: O(n)
        
        res = [0] * length
        for i in range(0, len(updates)):
            start = updates[i][0]
            end = updates[i][1]
            value = updates[i][2]
            res[start] += value
            if end + 1 <= length - 1:
                res[end+1] -= value
        
        for i in range(1, length):
            res[i] += res[i-1]
        
        return res
        
