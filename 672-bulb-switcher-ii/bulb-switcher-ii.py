# -*- coding:utf-8 -*-


#
# There is a room with n lights which are turned on initially and 4 buttons on the wall. After performing exactly m unknown operations towards buttons, you need to return how many different kinds of status of the n lights could be.
#
#
#
# Suppose n lights are labeled as number [1, 2, 3 ..., n], function of these 4 buttons are given below:
#
#
# Flip all the lights.
# Flip lights with even numbers.
# Flip lights with odd numbers.
# Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...
#
#
#
#
# Example 1:
#
# Input: n = 1, m = 1.
# Output: 2
# Explanation: Status can be: [on], [off]
#
#
#
#
# Example 2:
#
# Input: n = 2, m = 1.
# Output: 3
# Explanation: Status can be: [on, off], [off, on], [off, off]
#
#
#
#
# Example 3:
#
# Input: n = 3, m = 1.
# Output: 4
# Explanation: Status can be: [off, on, off], [on, off, on], [off, off, off], [off, on, on].
#
#
#
# Note:
# n and m both fit in range [0, 1000].
#
#


class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        
        # def com2(Sum):
            
            # resLists=[]
            # for j in range(0, Sum+1):
                # resLists.append([j, Sum-j])
            # return resLists
        
        # def com4(Sum):
            
            # resLists=[]
            # for k in range(0, Sum+1):
                # c1 = com2(k)
                # c2 = com2(Sum-k)
                
                # for cc1 in c1:
                    # for cc2 in c2:
                        # resLists.append(cc1+cc2)
            
            # return resLists
        
        # Com4=com4(m)
        # print Com4
        # tmp = [[] for i in range(0, 4)]
        
        # for c in Com4:
            # aa = (c[0] + c[2]) % 2
            # if aa not in tmp[0]:
                # tmp[0].append(aa)
            
            # bb = (c[0] + c[2] + c[3]) % 2
            # if bb not in tmp[1]:
                # tmp[1].append(bb)
            
            # cc = (c[0] + c[1]) % 2
            # if cc not in tmp[2]:
                # tmp[2].append(cc)
            
            # dd = (c[0] + c[1] + c[3]) % 2
            # if dd not in tmp[3]:
                # tmp[3].append(dd)
        
        # if n >=3:
            
        
        # Sum=1
        # for i in range(0, len(tmp)):
            # if (i == 0 and n>=3) or (i==1 and n>=1) or (i==2 and n>=2) or (i==3 and n>=4):
                # Sum *= len(tmp[i])
        # return Sum
        
        if(m==0): return 1
        if(n==1): return 2
        if(n==2 and m==1): return 3
        if(n==2): return 4
        if(m==1): return 4
        if(m==2): return 7
        if(m>=3): return 8
        return 8
    
