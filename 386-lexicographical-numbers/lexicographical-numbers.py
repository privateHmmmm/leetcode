# -*- coding:utf-8 -*-


#
# Given an integer n, return 1 - n in lexicographical order.
#
#
#
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
#
#
#
# Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
#


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
         
        lists = []
        cur = 1
        while len(lists) < n:
            lists.append(cur)
            if cur * 10 <= n:
                cur = cur * 10
            elif cur % 10 != 9 and (cur + 1)<=n:
                cur += 1
            else:
                while (cur / 10) % 10 == 9:
                    cur = cur/10
                cur = cur/10 + 1
        
        return lists
                
