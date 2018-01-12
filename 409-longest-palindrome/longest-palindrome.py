# -*- coding:utf-8 -*-


# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
#
# Example: 
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#
#


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        lens = 0
        dicts = collections.Counter(s)
        
        counter = dicts.values()
        one_flag = False
        
        for i in range(0, len(counter)):
            if counter[i] == 1:
                one_flag = True
            else:
                if one_flag == False and counter[i]%2==1:
                    one_flag = True
                lens += (counter[i]/2)*2
        
        if one_flag == True: lens +=1
        return lens
            
