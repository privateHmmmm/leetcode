# -*- coding:utf-8 -*-


#
#     Write a program to find the nth super ugly number.
#
#
#
#     Super ugly numbers are positive numbers whose all prime factors are in the given prime list
#     primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]
#  is the sequence of the first 12 super ugly numbers given primes
#     = [2, 7, 13, 19] of size 4.
#
#
#
#     Note:
#     (1) 1 is a super ugly number for any given primes.
#     (2) The given numbers in primes are in ascending order.
#     (3) 0 < k &le; 100, 0 < n &le; 106, 0 < primes[i] < 1000.
#     (4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        
        lists=[1]
        points=[0 for i in range(len(primes))]
        
        while len(lists) < n:
            Min = 2**31-1
            index = []
            for i in range(0, len(primes)):
                tmp = primes[i]*lists[points[i]]
                if Min > tmp:
                    indexes = [i] 
                    Min = min(Min, tmp)
                elif Min == tmp:
                    indexes.append(i)
        
            for index in indexes:
                points[index]+=1
            lists.append(Min)
        
        # print lists
        return lists[-1]
        
        
        
