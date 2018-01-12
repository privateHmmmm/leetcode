# -*- coding:utf-8 -*-


#
# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
#
#
#
# Example:
#
#
# Given "bcabc"
# Return "abc"
#
#
# Given "cbacdcbc"
# Return "acdb"
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        _map = {}
        for i in range(0, len(s)):
            _map[s[i]] = i
            
        lens = len(_map)
        res = [0 for i in range(0, lens)]
        start = 0
        for i in range(0, lens):
            end = min(_map.values())
            _min = '{' # next element of 'z'
            for j in range(start, end+1):
                if s[j] in _map and s[j] < _min:
                    _min = s[j]
                    start = j + 1
            res[i] = _min
            del _map[_min]
        
        return "".join(res)
        
