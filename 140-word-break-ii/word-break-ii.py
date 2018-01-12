# -*- coding:utf-8 -*-


#
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.
#
#
#
# Return all such possible sentences.
#
#
#
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
#
#
#
# A solution is ["cats and dog", "cat sand dog"].
#
#
#
# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
#


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        # memorized DFS
        wordDict = set(wordDict)
        _map = {}
        
        def helper(start):
            
            if start in _map:
                return _map[start]

            if start == len(s):
                return [""]
            
            res = []
            for i in range(start, len(s)):
                if s[start:i+1] in wordDict:
                    ll = helper(i+1)
                    for tmp in ll:
                        res.append(s[start:i+1] + (" " if tmp != "" else "") + tmp)
                     
            _map[start] = res
            return res
            
        return helper(0)
                
