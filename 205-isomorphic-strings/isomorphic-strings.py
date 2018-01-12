# -*- coding:utf-8 -*-


# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        lens = len(s) if len(s)==len(t) else -1
        if lens < 0:
            return False
        
        replace=0
        index = 0
        dict_s={}
        dict_t={}
        while index < lens:
            if s[index] not in dict_s and t[index] not in dict_t:
                dict_s[s[index]]=replace
                dict_t[t[index]]=replace
                replace +=1
            elif s[index] in dict_s and t[index] in dict_t:
                if dict_s[s[index]] != dict_t[t[index]]:
                    return False
            else:
                return False
            index +=1
        
        return True
                    
