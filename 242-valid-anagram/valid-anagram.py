# -*- coding:utf-8 -*-


# Given two strings s and t, write a function to determine if t is an anagram of s. 
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
#
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        dicts={}
        for chr in s:
            if chr in dicts:
                dicts[chr] +=1
            else:
                dicts[chr] = 1
        
        for chr in t:
            if chr not in dicts:
                return False
            else:
                dicts[chr] -=1
                if dicts[chr] == 0:
                    del dicts[chr]
            
        return not dicts
