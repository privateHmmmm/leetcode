# -*- coding:utf-8 -*-


#
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.
#
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
#
#
# Return true because "leetcode" can be segmented as "leet code".
#
#
#
# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
#


class TrieNode(object):
    
    def __init__(self):
    
        self.children = {}
        self.is_word = False

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        """
        # single DP
        wordDict = set(wordDict)
        
        DP=[False for i in range(0, len(s))]
        
        for i in range(0, len(s)):
            for j in range(0, i+1):
                if s[j:i+1] in wordDict and (j==0 or DP[j-1]):
                    DP[i]=True
        
        return DP[len(s)-1]
        # """
        
        # DP + prefix Tree
        def insert(root, word):
            
            for i in range(0, len(word)):
                if word[i] not in root.children:
                    root.children[word[i]] = TrieNode()
                root = root.children[word[i]]
            
            root.is_word = True
        
        root = TrieNode()
        for word in wordDict:
            insert(root, word)
            
        f = [False for i in range(0, len(s)+1)]
        f[0] = True
        
        for i in range(0, len(s)):
            if f[i]:
                r = root
                for j in range(i, len(s)):
                    if r != None and s[j] in r.children:
                        r = r.children[s[j]]
                        if r.is_word == True: f[j+1] = True
                    else:
                        break
    
        return f[-1]
                    
