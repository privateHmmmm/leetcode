# -*- coding:utf-8 -*-


# Given a pattern and a string str, find if str follows the same pattern.
#  Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.
#
# Examples:
#
# pattern = "abab", str = "redblueredblue" should return true.
# pattern = "aaaa", str = "asdasdasdasd" should return true.
# pattern = "aabb", str = "xyzabcxzyabc" should return false.
#
#
#
#
# Notes:
# You may assume both pattern and str contains only lowercase letters.
#


class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        _map = {}
        _set = set()
        
        def helper(p_idx, s_idx):
            
            if p_idx == len(pattern):
                return s_idx == len(str)
            
            if pattern[p_idx] in _map:
                match = _map[pattern[p_idx]]
                if str[s_idx:s_idx+len(match)] != match:
                    return False
                return helper(p_idx+1, s_idx+len(match))
            
            # for i in range(s_idx+1, len(str)+1):
            for i in range(s_idx+1, len(str)+p_idx+2-len(pattern)):
                if str[s_idx:i] in _set: continue
                _map[pattern[p_idx]] = str[s_idx:i]
                _set.add(str[s_idx:i])
                if True == helper(p_idx+1, i):
                    return True
                del _map[pattern[p_idx]]
                _set.remove(str[s_idx:i])
            return False
        
        return helper(0, 0)
        
