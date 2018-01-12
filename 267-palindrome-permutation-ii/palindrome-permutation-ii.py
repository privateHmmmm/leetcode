# -*- coding:utf-8 -*-


#
# Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.
#
#
# For example:
#
#
# Given s = "aabb", return ["abba", "baab"].
#
#
# Given s = "abc", return [].
#


class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        counter = collections.Counter(s)
        odd = ""
        for k, v in counter.iteritems():
            if v % 2 == 1:
                if odd != "": 
                    return []
                else:
                    odd = k
        
        res = []
        
        def helper(_str):
            
            if max(counter.values()) == 0: 
                res.append(_str)
                return        
            
            for k, v in counter.iteritems():
                if v != 0:
                    counter[k] -=2
                    helper(k + _str + k)
                    counter[k] +=2
        
        if odd:
            counter[odd] -=1
            helper(odd)
        else:
            helper("")
        return res
        
