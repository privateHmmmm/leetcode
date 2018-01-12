# -*- coding:utf-8 -*-


#
# Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.
#
# Example 1:
#
# Input: 12
# Output: 21
#
#
#
# Example 2:
#
# Input: 21
# Output: -1
#
#


class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n<10:
            return -1
        
        lists=list(str(n))
        for i in range(len(lists)-2, -1, -1):
            if lists[i]<lists[i+1]:
                break
        else:
            return -1
        print 'i: %d' %i
        
        for j in range(len(lists)-1, i-1, -1):
            if lists[j]>lists[i]:
                break
        print 'j: %d' %j
        
        saveI=lists[i]
        lists[i]=lists[j]
        lists[j]=saveI
        
        lists=lists[:i+1]+sorted(lists[i+1:])

        a=int("".join(lists))
        if a >2**31-1:
            return -1
        else:
            return a
    
    

