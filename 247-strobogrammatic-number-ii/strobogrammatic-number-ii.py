# -*- coding:utf-8 -*-


# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Find all strobogrammatic numbers that are of length = n. 
# For example,
# Given n = 2, return ["11","69","88","96"].
#


class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
        # dicts = {'6': '9', '1': '1', '8': '8'}
        
        def robot(remain, num):
            
            if remain == 0:
                res.append(num)
                return
            elif remain == 1:
                for i in '018':
                    res.append(num[0:len(num)/2]+i+num[len(num)/2:])
                return
            
            for k, v in {'6': '9', '1': '1', '9': '6', '8': '8'}.iteritems():
                robot(remain-2, num[0:len(num)/2] + k + v + num[len(num)/2:])
            if remain != n:
                robot(remain-2, num[0:len(num)/2] + '00' + num[len(num)/2:])
                
            return
        
        robot(n, "")
        return res
