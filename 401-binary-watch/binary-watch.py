# -*- coding:utf-8 -*-


# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
# Each LED represents a zero or one, with the least significant bit on the right.
#
# For example, the above binary watch reads "3:25".
#
# Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
#
# Example:
# Input: n = 1Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
#
#
# Note:
#
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
#
#


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
    
        """
        def count1Bits(n):
            
            count=0
            while (n > 0):
                count +=1
                n &= (n-1)
            return count
    
        def get_hours(hours):
            
            res=[]
            for i in range(0, 0b1100):
                if hours == count1Bits(i):
                    res.append(i)
            return res
            
        def get_minutes(minutes):
            
            res=[]
            for i in range(0, 0b111100):
                if minutes == count1Bits(i):
                    res.append(i)
            return res
        
        res=[]
        for hour in range(0, min(4, num)+1):
            
            minute=num-hour
            
            hours=get_hours(hour)
            minutes=get_minutes(minute)
            
            for i in hours:
                for j in minutes:
                    res.append("%d:%02d" %(i, j))
            
        return res
        """
        
        """
        method 2
        return ['%d:%02d' % (h, m)
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == num]
        """
        
        self.mins, self.hours = [], []
        hour_list, minute_list = [1, 2, 4, 8], [1, 2, 4, 8, 16, 32]
        res = []
        
        def helper_hour(idx, num, count):
            
            if num > 11: # !!!!!
                return
            
            if count == 0:
                self.hours.append(str(num))
                return
            
            if idx >= len(hour_list):
                return
            
            for i in range(idx, len(hour_list)):
                helper_hour(i+1, num+hour_list[i], count-1)
                
        def helper_mins(idx, num, count):
            
            if num > 59:  # !!!!
                return
            
            if count == 0:
                self.mins.append("%02d" %num)
                return
            
            if idx >= len(minute_list):
                return
            
            for i in range(idx, len(minute_list)):
                helper_mins(i+1, num+minute_list[i], count-1)
                
        for h in range(0, num+1):
            m = num - h
            helper_hour(0, 0, h)
            helper_mins(0, 0, m)
            for h1 in self.hours:
                for m1 in self.mins:
                    res.append("%s:%s" %(h1, m1))
            self.mins, self.hours = [], []
            
        return res    
