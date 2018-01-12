# -*- coding:utf-8 -*-


#
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
#
#
#
# Note: You may assume the string contain only lowercase letters.
#


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dicts = collections.Counter(s)
        
        for i in range(0, len(s)):
            if dicts[s[i]] == 1:
                return i
        
        return -1
            
