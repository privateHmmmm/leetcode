# -*- coding:utf-8 -*-


#
# Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.
#
#
#
# The input string does not contain leading or trailing spaces and the words are always separated by a single space.
#
#
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
#
#
# Could you do it in-place without allocating extra space?
#
#
# Related problem: Rotate Array
#
#
# Update (2017-10-16):
# We have updated the function signature to accept a character array, so please reset to the default code definition by clicking on the reload button above the code editor. Also, Run Code is now available!
#


class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        
        def reverse(i, j):
            
            left, right = i, j
            while left < right:
                tmp = str[left]
                str[left] = str[right]
                str[right] = tmp
                left += 1
                right -= 1
        
        reverse(0, len(str)-1)
        left = 0
        i = 0
        while i < len(str):
            if str[i] == ' ':
                reverse(left, i-1)
                left = i + 1
            i += 1
        
        if left < len(str): reverse(left, len(str)-1)
        return
            
                
        
