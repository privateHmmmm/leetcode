# -*- coding:utf-8 -*-


#
# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.
#
# Example 1:
#
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# Output: 
# "apple"
#
#
#
#
# Example 2:
#
# Input:
# s = "abpcplea", d = ["a","b","c"]
#
# Output: 
# "a"
#
#
#
# Note:
#
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.
#
#


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        
        
        
        def isSeq(s, seq):
            
            s_idx=0
            seq_idx=0
            
            while s_idx < len(s) and seq_idx < len(seq):
                if s[s_idx] == seq[seq_idx]:
                    s_idx+=1
                    seq_idx+=1
                else:
                    s_idx+=1
            
            if seq_idx == len(seq):
                return True
            else:
                return False
            
        longest=""
        for word in d:
            if isSeq(s, word) == True:
                if longest == "" or len(word) > len(longest) or (len(word)==len(longest) and cmp(word, longest) < 0):
                    longest=word
                
        return longest
            
        
                
                
