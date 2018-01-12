# -*- coding:utf-8 -*-


#
# Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.
#
#
# Examples: 
# "123", 6 -> ["1+2+3", "1*2*3"] 
# "232", 8 -> ["2*3+2", "2+3*2"]
# "105", 5 -> ["1*0+5","10-5"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []
#
#
# Credits:Special thanks to @davidtan1890 for adding this problem and creating all test cases.


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        
        # 2 + 3 * 4 = (5 - 3) + 3 * 4
        
        res = []
        
        def helper(idx, val, pre, path):
            
            if idx == len(num):
                if val == target: res.append(path)
                return
            
            for i in range(idx, len(num)):
                if i != idx and num[idx] == '0': break
                cur = int(num[idx:i+1])
                if idx == 0:
                    helper(i+1, cur, cur, str(cur))
                else:
                    helper(i+1, val + cur, cur, path + '+' + str(cur))
                    helper(i+1, val - cur, -cur, path + '-' + str(cur))
                    helper(i+1, (val - pre) + pre*cur, pre*cur, path + '*' + str(cur))

        helper(0, 0, 0, "")
        return res
                
