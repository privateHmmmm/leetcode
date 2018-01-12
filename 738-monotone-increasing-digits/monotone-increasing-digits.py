# -*- coding:utf-8 -*-


#
# Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.
#
# (Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)
#
#
# Example 1:
#
# Input: N = 10
# Output: 9
#
#
#
# Example 2:
#
# Input: N = 1234
# Output: 1234
#
#
#
# Example 3:
#
# Input: N = 332
# Output: 299
#
#
#
# Note:
# N is an integer in the range [0, 10^9].
#


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        # res = 0
        # remaining = N
        data = list(str(N))
        # remaining_len = len(data)
        
        for i in range(0, len(data)):
            remaining_len = len(data) - i - 1
            if remaining_len > 0 and int(data[i]*remaining_len) > int("".join(data[i+1:])):
                if data[i] != '0':
                    data[i] = str(int(data[i])-1)
                    data[i+1:] = '9'*remaining_len
                    break
                else:
                    data[i+1:] = '0'*remaining_len
                    break
            remaining_len -= 1
                
        return int("".join(data)) 
                
