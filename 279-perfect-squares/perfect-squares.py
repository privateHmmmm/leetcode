# -*- coding:utf-8 -*-


#
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
#
#
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """
        # TLE
        def perfectNum(n):
            
            index=1
            lists=[]
            
            while index**2<=n:
                lists.append(index**2)
                index +=1
            
            return lists
        
        curList=[]
        prefects=perfectNum(n)
        min_len=[n]
        
        def recursion(m, lists):
            
            if curList != [] and m == 0:
                min_len[0]=min(min_len[0], len(curList))
                return
            
            for i in range(len(lists)-1, -1, -1):
                if m-lists[i]>=0:
                    curList.append(lists[i])
                    recursion(m-lists[i], (lists[:i+1] if n-lists[i]>=lists[i] else lists[:i]))
                    # recursion(m-lists[i], lists[:i+1])
                    curList.pop()
            
        recursion(n, prefects)
        return min_len[0]
        """
        
        DP = [i for i in range(0, n+1)]
        # DP[0] = 0
        # DP[1] = 1
        
        for i in range(2, n+1):
            j = 1
            while j*j<=i:
                DP[i] = min(DP[i-j*j]+1, DP[i])
                j+=1
        return DP[n]
    
