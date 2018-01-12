# -*- coding:utf-8 -*-


# You are given a string representing an attendance record for a student. The record only contains the following three characters:
#
#
#
# 'A' : Absent. 
# 'L' : Late.
#  'P' : Present. 
#
#
#
#
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).    
#
# You need to return whether the student could be rewarded according to his attendance record.
#
# Example 1:
#
# Input: "PPALLP"
# Output: True
#
#
#
# Example 2:
#
# Input: "PPALLL"
# Output: False
#
#
#
#
#


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
 
#         flagA = False
        
#         for i in range(0, len(s)):
#             if s[i] == 'A':
#                 if flagA == True:
#                     return False
#                 else:
#                     flagA = True
#             else:
#                 if i>1 and s[i-2:i+1]=="LLL":
#                     return False
#         return True
            
        return not (s.count('A') > 1 or 'LLL' in s)
