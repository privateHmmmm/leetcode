# -*- coding:utf-8 -*-


# Given a digit string, return all possible letter combinations that the number could represent.
#
#
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
#
#
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
#
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.
#


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if not digits: return []
        
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        queue = [""]
        
        for i in range(0, len(digits)):
            lens = len(queue)
            for j in range(0, lens):
                for k in range(0, len(d[digits[i]])):
                    _str = queue[0] + d[digits[i]][k]
                    queue.append(_str)
                queue.pop(0)
        
        return queue
