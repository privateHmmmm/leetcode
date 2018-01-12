# -*- coding:utf-8 -*-


#
# Implement strStr().
#
#
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
#
#
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
#


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        """
        lo = 0
        while lo + len(needle) <= len(haystack):
            for k in range(0, len(needle)):
                if haystack[lo+k] != needle[k]:
                    lo = lo + 1
                    break
            else:
                return lo
        
        return -1
        """
        
    
        for left in range(0, len(haystack)-len(needle)+1):
            for n in range(0, len(needle)):
                if haystack[left+n] != needle[n]:
                    break
            else:
                return left
        
        return -1
        
                
                
             
            
            
            
            
            
