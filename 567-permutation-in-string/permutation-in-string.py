# -*- coding:utf-8 -*-


# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
#
# Example 1:
#
# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").
#
#
#
# Example 2:
#
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
#
#
#
# Note:
#
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
#
#


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        dicts = {}

        for c in s1:
            if c in dicts:
                dicts[c] += 1
            else:
                dicts[c] = 1

        left = 0
        right = 0
        
        while right < len(s2):
            if s2[right] in dicts and dicts[s2[right]] != 0:
                dicts[s2[right]] -= 1
                right += 1
                if right - left == len(s1):
                    return True
            else:
                # move right and restore dict
                if left < right:
                    dicts[s2[left]] += 1
                    left += 1
                else:
                    right +=1
                    left +=1
            
        return False
