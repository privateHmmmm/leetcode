# -*- coding:utf-8 -*-


# Write a function to generate the generalized abbreviations of a word.
#
#
#     Example:
#
# Given word = "word", return the following list (order does not matter):
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
#
#


class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        
        res = []
        
        def DFS(pos, _str, count):
            
            if pos >= len(word):
                res.append(_str + (str(count) if count > 0 else ""))
                return
            
            DFS(pos+1, _str, count + 1)  # turn to number
            DFS(pos+1, _str + (str(count) if count > 0 else "") + word[pos], 0) # reserve alpha
            
                
        DFS(0, "", 0)
        return res
                
