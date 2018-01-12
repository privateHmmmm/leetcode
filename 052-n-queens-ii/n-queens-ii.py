# -*- coding:utf-8 -*-


# Follow up for N-Queens problem.
#
# Now, instead outputting board configurations, return the total number of distinct solutions.
#
#


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        cnt = [0]
        check_col = [True for i in range(0, n)]
        check_slash = [True for i in range(0, 2*n-1)]  # [0,2*(n-1)]
        check_nslash = [True for i in range(0, 2*n-1)]    # [-(n-1), (n-1)] + (n-1) --> [0, 2*(n-1)]
        
        def dfs(row):
            
            if row >= n:
                cnt[0] +=1
                return 
            
            for col in range(0, n):
                if check_col[col] and check_slash[row+col] and check_nslash[n-1+row-col]:
                    check_col[col] = False
                    check_slash[row+col] = False
                    check_nslash[n-1+row-col] = False
                    dfs(row+1)
                    check_col[col] = True
                    check_slash[row+col] = True
                    check_nslash[n-1+row-col] = True
                    
        dfs(0)
        return cnt[0]
