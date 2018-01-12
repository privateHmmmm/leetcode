# -*- coding:utf-8 -*-


#
# Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.
#
#
# Example 1:
#
# Input:
# s = "aaabb", k = 3
#
# Output:
# 3
#
# The longest substring is "aaa", as 'a' is repeated 3 times.
#
#
#
# Example 2:
#
# Input:
# s = "ababbc", k = 2
#
# Output:
# 5
#
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
#
#


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        def helper(uniqueNum):
        
            sTable = [0]*128
            d = 0
            uniqueCount = 0
            begin, end = 0, 0
            noLessThanK = 0
            res = 0
            
            while end < len(s):
                c = ord(s[end])
                end += 1
                if sTable[c] == 0:
                    uniqueCount += 1
                sTable[c] += 1
                if sTable[c] == k:
                    noLessThanK += 1
                while uniqueCount > uniqueNum:
                    # print begin
                    tmp = ord(s[begin])
                    sTable[tmp] -= 1
                    if sTable[tmp] == 0:
                        uniqueCount -= 1
                    if sTable[tmp] == k-1:
                        noLessThanK -= 1
                    begin += 1
                    # print uniqueCount, uniqueNum
                
                if noLessThanK == uniqueCount and uniqueCount == uniqueNum:
                    res = max(res, end-begin)
            return res
        
        res = 0
        for i in range(1, 27):
            res = max(res, helper(i))
        return res
                
