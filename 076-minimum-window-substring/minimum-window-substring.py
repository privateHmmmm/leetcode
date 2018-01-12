# -*- coding:utf-8 -*-


#
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
#
#
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
#
#
# Minimum window is "BANC".
#
#
#
# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".
#
#
# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
#


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        """
        cnt = {}
        for i in range(0, len(t)):
            cnt[t[i]] = cnt.get(t[i], 0) + 1
        
        _from = 0
        total = len(t)
        _min = 2**31-1
        j = 0
        for i in range(0, len(s)):
            if cnt.get(s[i], 0) > 0:
                total -= 1
            cnt[s[i]] = cnt.get(s[i], 0) - 1    
            while total == 0:
                if i - j + 1 < _min:
                    _min = i - j + 1
                    _from = j 
                cnt[s[j]] = cnt.get(s[j], 0) + 1
                if cnt[s[j]] > 0:
                    total += 1
                j += 1
        
        return "" if _min == 2**31-1 else s[_from:_from+_min]
        """
                
        table = [0] * 128
        count = 0
        begin, end = 0, 0
        d = 2**31-1
        head = 0
        
        for i in range(0, len(t)):
            table[ord(t[i])] += 1
        
        while end < len(s):
            c = ord(s[end])
            end += 1
            table[c] -= 1
            if table[c] >= 0: count += 1
            while count == len(t):
                if end-begin < d:
                    d = end-begin
                    head = begin
                tmp = ord(s[begin])
                begin += 1
                table[tmp] += 1
                if table[tmp] > 0:
                    count -= 1
        
        return "" if d == 2**31-1 else s[head:head+d]
            
