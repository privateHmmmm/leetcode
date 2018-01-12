# -*- coding:utf-8 -*-


#
# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
#
# Note: The input string may contain letters other than the parentheses ( and ). 
#
#
#
# Examples:
#
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]
#
#
#
# Credits:Special thanks to @hpplayer for adding this problem and creating all test cases.


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        def isValid(s):
            
            count = 0
            for i in range(0, len(s)):
                if s[i] == '(':
                    count += 1
                elif s[i] == ')':
                    count -= 1
                if count < 0: return False
            
            return True if count == 0 else False
        
        def calRemove(s):
            
            l, r = 0, 0
            for i in range(0, len(s)):
                if s[i] == '(':
                    l += 1
                elif s[i] == ')':
                    if l == 0: 
                        r += 1
                    else:
                        l -= 1
            return l, r
        
        res = []
        
        def dfs(s, start, l, r):
            
            if l == 0 and r == 0:
                if isValid(s): res.append(s)
                return
            
            for i in range(start, len(s)):
                
                if i != start and s[i-1] == s[i]: continue
                
                if r > 0:
                    if s[i] == ')':
                        newS = s[0:i] + s[i+1:]
                        dfs(newS, i, l, r-1)
                elif l > 0:
                    if s[i] == '(':
                        newS = s[0:i] + s[i+1:]
                        dfs(newS, i, l-1, r)
        
        l, r = calRemove(s)
        dfs(s, 0, l, r)
        return res
            
