# -*- coding:utf-8 -*-


# Related to question Excel Sheet Column Title
# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#     A -&gt; 1
#     B -&gt; 2
#     C -&gt; 3
#     ...
#     Z -&gt; 26
#     AA -&gt; 27
#     AB -&gt; 28 
#
# Credits:Special thanks to @ts for adding this problem and creating all test cases.


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res = 0
        for i in range(0, len(s)):
            res = res*26 + ord(s[i]) - ord('A') + 1
        
        return res
        
