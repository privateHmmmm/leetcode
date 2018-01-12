# -*- coding:utf-8 -*-


# Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.
#
# Note:
#
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
# Input length is less than 50,000.
#
#
#
# Example 1:
#
# Input: "owoztneoer"
#
# Output: "012"
#
#
#
# Example 2:
#
# Input: "fviefuro"
#
# Output: "45"
#
#


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        Counter = collections.Counter(s)
        lists = [0 for i in range(0, 10)]
            
        ids =    ['z',    'w',   'u',    'x',   'f',    's',     'r',     'o',    'g',    'i']
        remain = ['zero', 'two', 'four', 'six', 'five', 'seven', 'three', 'one',  'eight', 'nine']
        rep = [   0,      2,     4,      6,     5,       7,       3,       1,      8,       9]
        for i in range(0, 10):
            if ids[i] in Counter and Counter[ids[i]] != 0:
                cnt = Counter[ids[i]]
                lists[rep[i]] = cnt 
                for c in remain[i]:
                    Counter[c] -= cnt
        
        res =''
        for i in range(0, 10):
            res += str(i)*lists[i]
        return res        
              
