# -*- coding:utf-8 -*-


# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        method one, but the performance is very bad
        list = []
        length_s = len(s)
        for i in range(0, length_s):
            if s[i] in s[i+1:]:
                list.append(s[i+1:].find(s[i]))
            else:
                list.append(length_s-i-1)
        
        #print list
        #list: 后面还能有多少个数
        
        max_length = 0
        for i in range(0, length_s):
            if max_length > length_s - i:
                break
            #print 'i: %d' %i
            j = 1
            
            end_index = i + list[i]
            while i+j < end_index:
                #print i+j, end_index
                if (i + j + list[i + j]) < end_index:
                    end_index = i + j + list[i + j]
                j += 1
            #print 'max_length: %d' % (end_index - i + 1)
            if (end_index - i + 1) > max_length:
                max_length = end_index - i + 1
            
        return max_length
        """
                
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            
            used[c] = i

        return max_length
                
                
            
            
            
            
            
            
        
