# -*- coding:utf-8 -*-


# Given a pattern and a string str, find if str follows the same pattern.
#  Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
#
# Examples:
#
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
#
#
#
#
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
#
#
# Credits:Special thanks to @minglotus6 for adding this problem and creating all test cases.


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        _map = {}
        _set = set()
        _list = str.split(" ")
        if len(pattern) != len(_list): return False
        
        i, j = 0, 0
        while i < len(pattern):
            if pattern[i] not in _map and _list[i] in _set:
                return False
            if pattern[i] in _map and _map[pattern[i]] != _list[i]:
                return False
            _map[pattern[i]] = _list[i]
            _set.add(_list[i])
            i += 1

        return True
            
