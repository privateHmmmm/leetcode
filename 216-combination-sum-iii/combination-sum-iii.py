# -*- coding:utf-8 -*-


#
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
#
#
#  Example 1:
# Input:  k = 3,  n = 7
# Output: 
#
# [[1,2,4]]
#
#
#  Example 2:
# Input:  k = 3,  n = 9
# Output: 
#
# [[1,2,6], [1,3,5], [2,3,4]]
#
#
#
# Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        """
        ans = []
        
        for i in range(0, 1<<9):
            tmp = []
            for j in range(0, 9):
                if i&(1<<j) != 0:
                    tmp.append(j+1)
                    
            if len(tmp)==k and sum(tmp) == n:
                ans.append(tmp)
                
        return ans
        """
        
        ans = []
        path = []
        
        def helper(idx, _sum):
            
            if _sum == n and len(path) == k:
                ans.append(copy.copy(path))
                return 
            
            if idx >= 9 or _sum + (idx+1) > n or len(path) >= k:
                return 
            
            for i in range(idx, 9):
                path.append(i+1)
                helper(i+1, _sum+(i+1))
                path.pop()
        
        helper(0, 0)
        return ans
    
        
