# -*- coding:utf-8 -*-


# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below. 
#
#
#
#
#
#
#
# Example 1:
#
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
#
#
#
# Note:
#
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.
#
#


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        dicts=collections.Counter('qwertyuiopQWERTYUIOP')
        dicts.update('asdfghjklASDFGHJKL'*2)
        dicts.update('zxcvbnmZXCVBNM'*3)
        res=[]
        
        for i in range(len(words)):
            for j in range(0, len(words[i])):
                if words[i][j] not in dicts:
                    break
                else:
                    if j >0 and dicts[words[i][j]] != dicts[words[i][j-1]]:
                        break
            else:
                res.append(words[i])
        
        return res
        
        
        
