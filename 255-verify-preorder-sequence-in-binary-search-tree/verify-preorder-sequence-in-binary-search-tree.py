# -*- coding:utf-8 -*-


# Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.
#
# You may assume each number in the sequence is unique.
#
# Follow up:
# Could you do it using only constant space complexity?


class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        
        stack = []
        _min = -2^31
        
        for num in preorder:
            if num < _min:
                return False
            
            while stack and num>stack[-1]:
                _min = stack.pop()
            
            stack.append(num)
        
        return True
    
