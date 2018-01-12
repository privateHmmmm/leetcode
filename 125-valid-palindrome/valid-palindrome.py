# -*- coding:utf-8 -*-


#
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
#
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
#
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.
#


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        
        first, last = 0, len(s)-1
        
        while first<last:
            while first<last and not (s[first].isdigit() or s[first].isalpha()):
                first +=1
            
            while first<last and not (s[last].isdigit() or s[last].isalpha()):
                last -=1
                
            if first >= last: return True
            if s[first].lower() != s[last].lower(): return False
            first +=1
            last -=1
        
        return True
        
        
#         first = 0
#         last = len(s)-1
        
#         while first <= last:
#             while not (s[first].isdigit() or s[first].isalpha()):
#                 first += 1
#                 if first > last:
#                     return True
#             while not (s[last].isdigit() or s[last].isalpha()):
#                 last -= 1
#                 if first > last:
#                     return True
            
#             #if first > last:
#             #    break
            
#             if s[first].lower() != s[last].lower():
#                 return False
                
#             first += 1
#             last -= 1
            
#         return True
            
        
        
