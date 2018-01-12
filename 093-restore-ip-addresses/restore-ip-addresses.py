# -*- coding:utf-8 -*-


# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
#
# For example:
# Given "25525511135",
#
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
#


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        def helper(_str, index, count):
            
            # print _str, index, count
            if count == 4:
                if index == len(s):
                    # print _str
                    res.append(_str)
                return
            
            for i in range(1, 4):
                if index + i > len(s): return
                tmp = s[index:index+i]
                if (tmp[0] == '0' and len(tmp) > 1) or (int(tmp) > 255):
                    continue
                
                helper(_str + ("" if _str == "" else ".") + tmp, index+i, count+1)
        
        res = []
        helper("", 0, 0)
        return res
                
