# -*- coding:utf-8 -*-


#
# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
#
#
# For example,
#
# 123 -> "One Hundred Twenty Three"
# 12345 -> "Twelve Thousand Three Hundred Forty Five"
# 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"


class Solution(object):
    
    LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    THOUSANDS = ["", "Thousand", "Million", "Billion"]
        
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
             
        def helper(num):
            # take care of num < 1000
        
            if num == 0: 
                return ""
            elif num < 20:
                return Solution.LESS_THAN_20[num] + " "
            elif num < 100:
                return Solution.TENS[num/10] + " " + helper(num % 10)
            else:
                return Solution.LESS_THAN_20[num/100] + ' Hundred ' + helper(num % 100)
            
        if num == 0: return "Zero"
        res = ""
        i = 0
        
        while num > 0:
            if num % 1000 != 0:
                res = helper(num % 1000) + Solution.THOUSANDS[i] + " " + res
            num /= 1000    
            i += 1
        
        return res.strip()
   
