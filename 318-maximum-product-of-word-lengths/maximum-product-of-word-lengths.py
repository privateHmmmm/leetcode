# -*- coding:utf-8 -*-


#
#     Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters.
#     You may assume that each word will contain only lower case letters.
#     If no such two words exist, return 0.
#
#
#
#     Example 1:
#
#
#     Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
#     Return 16
#     The two words can be "abcw", "xtfn".
#
#
#     Example 2:
#
#
#     Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
#     Return 4
#     The two words can be "ab", "cd".
#
#
#     Example 3:
#
#
#     Given ["a", "aa", "aaa", "aaaa"]
#     Return 0
#     No such pair of words.    
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        res = 0
        mask = [0 for i in range(0, len(words))]
        
        for i in range(0, len(words)):
            val = 0
            for j in range(0, len(words[i])):
                val |= (1 << (ord(words[i][j])-97))
            mask[i] = val
        
        for i in range(0, len(words)):
            for j in range(i+1, len(words)):
                if mask[i]&mask[j]==0:
                    res = max(res, len(words[i])*len(words[j]))
        
        return res
    
