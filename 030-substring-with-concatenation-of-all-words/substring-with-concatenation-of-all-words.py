# -*- coding:utf-8 -*-


#
# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
#
#
#
# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]
#
#
#
# You should return the indices: [0,9].
# (order does not matter).
#


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        # timeout: (len(s)*len(word))
        _map = {}
        for word in words:
            _map[word] = _map.get(word, 0) + 1
        
        res = []
        m = len(words)
        n = len(words[0])
        for i in range(0, len(s)-n*m+1):
            _map2 = copy.copy(_map)
            j = i
            while j < i + n*m:
                if s[j:j+n] not in _map2 or _map2[s[j:j+n]] == 0:
                    break
                _map2[s[j:j+n]] -= 1
                j += n
            if j == i+n*m:
                res.append(i)
        
        return res
                
            
            
        
        
        
        
        
        
#         _map = {}
#         for word in words:
#             _map[word] = _map.get(word, 0) + 1
        
#         res = []
#         n = len(words)
#         m = len(words[0])
#         for i in range(0, len(s)-n*m+1):
#             map2 = copy.copy(_map)
#             j = i
#             while j < i+n*m:
#                 if s[j:j+m] not in map2 or map2[s[j:j+m]] < 1:
#                     break
#                 map2[s[j:j+m]] -= 1
#                 j += m
#             if j == i+n*m: res.append(i)
        
#         return res
                
