# -*- coding:utf-8 -*-


# Write a function to find the longest common prefix string amongst an array of strings.
#


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # str=["123", "abc", "xyz"] zip(*str) ----> [("1", "a", "x"), ("2", "b", "y"), ("3", "c", "z")]
        # str=["123", "abc", "x"] zip(*str) ---> [("1", "a", "x")]
        
        # if not strs: return ""
        # tmp = list(zip(*strs))
        # for i in range(0, len(tmp)):
        #     if len(set(tmp[i])) > 1:
        #         return strs[0][:i]
        # else:
        #     return strs[0][:len(tmp)]
        
        if not strs: return ""
        candidate = strs[0]
        i = 0
        while i < len(candidate):
            for j in range(1, len(strs)):
                if i > len(strs[j])-1 or strs[j][i] != candidate[i]:
                    return candidate[:i]
            i += 1
        
        return candidate
                    
        
