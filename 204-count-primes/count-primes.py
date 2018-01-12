# -*- coding:utf-8 -*-


# Description:
# Count the number of prime numbers less than a non-negative number, n.
#
# Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """
        NotPrime=[False]*n

        for i in range(2, int(math.sqrt(n))+1):
            for j in range(i, n):
                if i*j >=n:
                    break
                NotPrime[i*j]=True
        #rint 'eeeeee'
        count = 0
        for i in range(2, n):
            if NotPrime[i] == False:
                count +=1
                
        return count
        """
        
        if n <= 2:
            return 0
        
        prime = [True] * n
        prime[:2] = [False, False]
        for base in xrange(2, int((n - 1) ** 0.5) + 1):
            if prime[base]:
                prime[base ** 2::base] = [False] * len(prime[base ** 2::base])
        return sum(prime)
    
    
                
