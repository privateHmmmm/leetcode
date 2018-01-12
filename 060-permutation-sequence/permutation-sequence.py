# -*- coding:utf-8 -*-


# The set [1,2,3,&#8230;,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
#
#
#
# Given n and k, return the kth permutation sequence.
#
# Note: Given n will be between 1 and 9 inclusive.


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        number = map(str, range(1, n+1))
        
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1]*i)
        
        res = ""
        k = k - 1
        for i in range(1, n+1):
            index = k/factorial[n-i]
            k = k % factorial[n-i]
            res += str(number[index])
            del number[index]
    
        return res
    
