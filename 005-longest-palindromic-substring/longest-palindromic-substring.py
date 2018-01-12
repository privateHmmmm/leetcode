# -*- coding:utf-8 -*-


# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example:
#
# Input: "babad"
#
# Output: "bab"
#
# Note: "aba" is also a valid answer.
#
#
#
# Example:
#
# Input: "cbbd"
#
# Output: "bb"
#
#


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        """
        if not s: return ""
        
        max_len = 1; res = [s[0]]
        
        # odd length
        for i in range(0, len(s)):
            tmp = 1
            for j in range(1, i+1):
                if i+j<len(s) and s[i+j] == s[i-j]: 
                    tmp +=2
                else:
                    break
            if tmp > max_len:
                max_len = tmp
                res[0] = s[i-max_len/2:i+max_len/2+1] 
                
                
        # even length
        for i in range(0, len(s)):
            tmp = 0
            for j in range(0, i+1):
                if i+1+j<len(s) and i-j>=0 and s[i-j] == s[i+1+j]:
                    tmp +=2
                else:
                    break
            
            if tmp > max_len:
                max_len = tmp
                res[0] = s[i-max_len/2+1:i+1+max_len/2]
        
        return res[0]
        """
        
        # ------my------j------------_id-------------i------mx------
        
        #      #1#2#2#1#2#3#2#1#
        #      12125214121612121   
        
        ss="#"
        for i in range(0, len(s)):
            ss+=(s[i]+'#')
            
        p = [0 for i in range(0, len(ss))]
        p[0] = 1
        _id = 0; 
        mx = 1;
        for i in range(1, len(ss)):
            if mx>i:
                # p[i] = min(p[2*_id-i], mx-i)
                if p[2*_id-i] < mx-i:
                    p[i] = p[2*_id-i]
                    continue
                else:
                    p[i] = mx-i
                
            else:
                p[i] = 1
            
            # if p[i] 
            while (i+p[i]<len(ss) and i-p[i]>=0 and ss[i+p[i]] == ss[i-p[i]]):
                p[i] +=1
            if mx<i+p[i]: 
                mx=i+p[i]
                _id = i
        
        max_len = max(p)
        index = p.index(max_len)
        start_index = (index-max_len+1)/2
        return s[start_index:start_index+max_len-1]    
    
