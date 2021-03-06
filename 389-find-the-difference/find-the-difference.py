# -*- coding:utf-8 -*-


#
# Given two strings s and t which consist of only lowercase letters.
#
# String t is generated by random shuffling string s and then add one more letter at a random position.
#
# Find the letter that was added in t.
#
# Example:
#
# Input:
# s = "abcd"
# t = "abcde"
#
# Output:
# e
#
# Explanation:
# 'e' is the letter that was added.
#


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        """
        dicts={}
        for i in s:
            dicts[i]=dicts.get(i, 0)+1
        
        for j in t:
            dicts[j]=dicts.get(j, 0)-1
        
        for k in dicts:
            if dicts[k] != 0:
                return k
        """
        
        c=ord(t[-1])
        for i in range(0, len(s)):
            c ^= ord(s[i])
            c ^= ord(t[i])
        
        return chr(c)
