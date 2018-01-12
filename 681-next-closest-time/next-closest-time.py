# -*- coding:utf-8 -*-


# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.
#
# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
#
# Example 1:
#
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
#
#
#
# Example 2:
#
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
#
#


class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        lists = list(time)
        lists = [int(lists[i]) for i in range(0, len(lists)) if lists[i] != ':']        
        
        flag = False
        minutes = 10*lists[2]+lists[3]
        for i in range(minutes+1, 60):
            tenmin = i/10
            mins = i-10*tenmin
            if tenmin in lists and mins in lists:
                lists[2] = tenmin
                lists[3] = mins
                flag = True
                break
                
        if flag == False:
            hours = 10*lists[0]+lists[1]
            for i in range(hours+1, 24):
                tenhour = i/10
                hour = i-10*tenhour
                if tenhour in lists and hour in lists:
                    lists[2] = min(lists)
                    lists[3] = min(lists)
                    lists[0] = tenhour
                    lists[1] = hour
                    flag = True
                    break
            
            if flag == False:
                lists[:] = [min(lists)]*4

        return "%d%d:%d%d" %(lists[0], lists[1], lists[2], lists[3])
        
