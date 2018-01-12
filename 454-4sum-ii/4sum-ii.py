# -*- coding:utf-8 -*-


# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
#
# To make problem a bit easier, all A, B, C, D have same length of N where 0 &le; N &le; 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
#
# Example:
#
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# Output:
# 2
#
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
#
#


from itertools import permutations
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        
        """
        # My solution
        lenA=len(A)
        dict1 = collections.Counter()
        dict2 = collections.Counter()
        for i in range(0, lenA):
            for j in range(0, lenA):
                dict1[A[i]+B[j]] += 1
                dict2[C[i]+D[j]] += 1
            
        res = 0
        for k1 in dict1:
            if -k1 in dict2:
                res += dict1[k1]*dict2[-k1]
        
        return res
        """
    

        a1 = collections.Counter(A)
        a2 = collections.Counter(B)
        a3 = collections.Counter(C)
        a4 = collections.Counter(D)
        
        A1 = {}
        for i1, v1 in a1.iteritems():
            for i2, v2 in a2.iteritems():
                tmp = i1 + i2
                if tmp < 2**31 or tmp >  -2**31 - 1:
                    if tmp not in A1:
                        A1[tmp] = v1*v2 
                    else:
                        A1[tmp] += v1*v2
                    
        ans = 0
        for i1, v1 in a3.iteritems():
            for i2, v2 in a4.iteritems():
                tmp = i1 + i2               
                if tmp < 2**31 or tmp >  -2**31 - 1:
                    if -tmp in A1:
                        ans += v1*v2*A1[-tmp]       
          
        return ans if ans < 2**31 - 1 else  2**31 - 1 
        
