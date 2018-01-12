# -*- coding:utf-8 -*-


#
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
#
# Return all possible palindrome partitioning of s.
#
#
# For example, given s = "aab",
#
# Return
#
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]
#
#


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        # it's not good to use DP because of the deep copy
        """
        result_list=[]
        cur_list=[]
        
        def isPalindrome(start, end):
            
            if start==end:
                return True
            
            while end > start:
                if s[start]!=s[end]:
                    return False
                start +=1
                end -=1
            return True
        
        def recursion(start):
            
            if cur_list != [] and start >= len(s):
                result_list.append(copy.copy(cur_list))
            
            for i in range(start, len(s)):
                if isPalindrome(start, i):
                    cur_list.append(s[start:i+1])
                    recursion(i+1)
                    cur_list.pop()
        
        recursion(0)
        return result_list
        """
    
        palindrome = [[False for i in range(len(s))] for j in range(0, len(s))]
        
        for i in range(0, len(s)):
            palindrome[i][i] = True
        
        for r in range(2, len(s)+1):
            for i in range(0, len(s)+1-r):
                j = i+r-1
                if r == 2:
                    if s[i] == s[j]: palindrome[i][j] = True
                else:
                    if s[i] == s[j] and palindrome[i+1][j-1] == True: palindrome[i][j] = True
        
        res = []
        cur = []
        
        def robot(idx):
            
            if idx>=len(s):
                res.append(copy.copy(cur))
                return
            
            for i in range(idx, len(s)):
                if palindrome[idx][i] == True:
                    cur.append(s[idx:i+1])
                    robot(i+1)
                    cur.pop()
        
        robot(0)
        return res
                    
