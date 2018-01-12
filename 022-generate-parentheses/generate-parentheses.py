# -*- coding:utf-8 -*-


#
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#
#
# For example, given n = 3, a solution set is:
#
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        """
        # backtrace method
        res = []
        def backtrace(_open, _close, _str):
            
            if _open + _close == 2*n:
                res.append(_str)
                return 
            
            if _open < n:
                backtrace(_open+1, _close, _str+'(')
            
            if _open > _close:
                backtrace(_open, _close+1, _str+')')
            
        backtrace(1, 0, '(')
        return res
        """
        
        _map = collections.defaultdict(list)
        _map[0] = [""]
        _map[1] = ["()"]
        def _gen(i):
        
            if i in _map:
                return _map[i]
            
            for j in range(0, i):
                for k1 in _gen(j):
                    for k2 in _gen(i-j-1):
                        _map[i].append(k1+'('+k2+')')
            
            return _map[i]
        
        return _gen(n)
                

