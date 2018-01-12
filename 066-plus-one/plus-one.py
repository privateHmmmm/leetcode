# -*- coding:utf-8 -*-


# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of the list.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            num = digits[i]+carry
            digits[i] = num%10
            carry = num/10
        
        if carry:
            digits.insert(0, carry)
        return digits
