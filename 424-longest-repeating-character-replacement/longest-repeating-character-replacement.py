# -*- coding:utf-8 -*-


# Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.
#
# Note:
# Both the string's length and k will not exceed 104.
#
#
#
# Example 1:
#
# Input:
# s = "ABAB", k = 2
#
# Output:
# 4
#
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
#
#
#
#
# Example 2:
#
# Input:
# s = "AABABBA", k = 1
#
# Output:
# 4
#
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
#
#


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        lo = 0
        hi = 0
        Max = 0
        table = collections.Counter()
        
        while hi < len(s):
            table[s[hi]] +=1
            hi +=1
            while hi-lo-max(table.values())>k:
                table[s[lo]]-=1
                lo+=1
            Max = max(Max, hi-lo)
        return Max
                
