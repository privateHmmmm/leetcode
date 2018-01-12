# -*- coding:utf-8 -*-


# Given an array of strings, group anagrams together.
#
#
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:
#
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
# Note: All inputs will be in lower-case.


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # O(m*n*logn) m = len(strs), n = len(strs[0])
        
        dicts = {}
        for _str in strs:
            tmp = ''.join(sorted(_str))
            dicts[tmp] = dicts.get(tmp, []) + [_str]
        
        return dicts.values()
    
