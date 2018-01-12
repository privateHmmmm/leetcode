# -*- coding:utf-8 -*-


#
# Given a string, your task is to count how many palindromic substrings in this string.
#
#
#
# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters. 
#
#
# Example 1:
#
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
#
#
# Example 2:
#
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
#
# Note:
#
# The input string length won't exceed 1000.
#
#


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """
        res = len(s)
        for i in range(0, len(s)):
            # odd lens
            j = 1
            while i-j >=0 and i+j<len(s):
                if s[i-j] == s[i+j]:
                    res +=1
                else:
                    break
                j +=1
            
            # even lens
            j = 0
            while i-j>=0 and i+j+1<len(s):
                if s[i-j] == s[i+j+1]:
                    res +=1
                else:
                    break
                j+=1

        return res
        """
        
        #      #1#2#2#1#2#3#2#1#
        #      12125214121612121   
        
        ss="#"
        for i in range(0, len(s)):
            ss+=(s[i]+'#')
                
        _id = 0; mx = 1; 
        p = [1 for i in range(0, len(ss))]
        
        for i in range(1, len(ss)):
            if i < mx:
                if p[2*_id-i] < mx-i:
                    p[i] = p[2*_id-i]
                    continue
                else:
                    p[i] = mx-i
            else:
                p[i] = 1
                
            while (i+p[i]<len(ss) and i-p[i]>=0 and ss[i+p[i]] == ss[i-p[i]]):
                p[i] +=1
            if mx<i+p[i]: 
                mx=i+p[i]
                _id = i
        
        cnt = 0
        for i in range(0, len(p)):
            cnt += (p[i])/2
        return cnt
        
                
            
            
            
        
        
        
        
        
