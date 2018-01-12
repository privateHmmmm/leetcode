# -*- coding:utf-8 -*-


#
# Given a word, you need to judge whether the usage of capitals in it is right or not.
#
#
#
# We define the usage of capitals in a word to be right when one of the following cases holds:
#
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if it has more than one letter, like "Google".
#
# Otherwise, we define that this word doesn't use capitals in a right way.
#
#
#
# Example 1:
#
# Input: "USA"
# Output: True
#
#
#
# Example 2:
#
# Input: "FlaG"
# Output: False
#
#
#
# Note:
# The input will be a non-empty word consisting of uppercase and lowercase latin letters.
#


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        if not word:
            return True
        
        def allCaptial(s):
            
            for i in range(0, len(s)):
                if s[i]<'A' or s[i]>'Z':
                    return False
            return True
        
        def allLowerCase(s):
            
            for i in range(0, len(s)):
                if s[i]<'a' or s[i]>'z':
                    return False
            return True
                
        if word[0] >= 'A' and word[0] <='Z':
            return allLowerCase(word[1:]) or allCaptial(word[1:])
        else:
            return allLowerCase(word[1:])
        
        
        
