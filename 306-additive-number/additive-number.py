# -*- coding:utf-8 -*-


# Additive number is a string whose digits can form additive sequence.
#
# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
#
#
# For example:
# "112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# "199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
# 1 + 99 = 100, 99 + 100 = 199
#
#
#
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
#
#
# Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.
#
#
# Follow up:
# How would you handle overflow for very large input integers?
#
#
# Credits:Special thanks to @jeantimex for adding this problem and creating all test cases.


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        if len(num) <=2 : return False
        
        def dfs(idx, pre1, pre2, count):
            
            if idx == len(num):
                return count > 2

            min_lens = 1 if not pre1 else max(len(pre1), len(pre2))
            for lens in range(min_lens, len(num)+1-idx):
                tmp = num[idx:idx+lens]
                
                if tmp[0] == '0' and len(tmp) > 1: return False
                if pre1 and pre2:
                    _sum = int(pre1) + int(pre2) 
                    if _sum < int(tmp): 
                        return False
                    elif _sum > int(tmp): 
                        continue
                if dfs(idx+lens, pre2, tmp, count + 1) == True:
                    return True
            return False
        
        return dfs(0, "", "", 0)
                    
            
