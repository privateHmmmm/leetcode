# -*- coding:utf-8 -*-


# Write a function that takes a string as input and reverse only the vowels of a string.
#
#
# Example 1:
# Given s = "hello", return "holle".
#
#
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
#
#
# Note:
# The vowels does not include the letter "y".
#


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        lists=list(s)
        vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        left=0
        right=len(lists)-1
        
        while left < right:
            while left < right and lists[left] not in vowels:
                left +=1
            
            while right > left and lists[right] not in vowels:
                right -=1
            
            if left < right:
                save=lists[left]
                lists[left]=lists[right]
                lists[right]=save
                left +=1
                right -=1
        
        return "".join(lists)
    
            
