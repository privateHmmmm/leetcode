# -*- coding:utf-8 -*-


#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
#
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
#


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
            return s
            
        zz = ''
        len_s = len(s)
        period = 2*numRows - 2
        real_row = min(len_s, numRows)
        for i in range(0, real_row):
            index = i
            while index < len_s:
                zz += s[index]
                if i > 0 and i < real_row - 1:
                    index1 = index + period - 2*i
                    if index1 >= 0 and index1 < len_s:  
                        zz += s[index1]
                    
                index = index + period
        
        return zz
        
        
