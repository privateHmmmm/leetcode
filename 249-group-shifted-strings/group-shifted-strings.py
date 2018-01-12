# -*- coding:utf-8 -*-


# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
# "abc" -> "bcd" -> ... -> "xyz"
#
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.
#
# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
# A solution is:
#
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        
        _map = collections.defaultdict(list)
        
        for _str in strings:
            key = "a"
            offset = ord(_str[0]) - ord('a')
            for i in range(1, len(_str)):
                key += (chr(ord(_str[i])-offset) if ord(_str[i])-offset>=ord('a') else chr(ord(_str[i])-offset+26))
            _map[key].append(_str)
    
        res = []
        for l in _map.values():
            l.sort()
            res.append(l)
        return res
                
