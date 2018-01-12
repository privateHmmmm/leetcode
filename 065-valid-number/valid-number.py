# -*- coding:utf-8 -*-


# Validate if a given string is numeric.
#
#
# Some examples:
# "0" => true
# "   0.1  " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
#
#
# Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
#
#
#
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
#


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        """
        (+-)10.234e56
        """
        
        s = s.strip()
        numSeen = False
        numAfterE = True
        eSeen = False
        pointSeen = False
        
        for i in range(0, len(s)):
            if s[i].isdigit() == True:
                numSeen = True
                numAfterE = True
            elif s[i] == 'e':  # not e1, not e1e2
                if eSeen or not numSeen: 
                    return False
                eSeen = True
                numAfterE = False
            elif s[i] == '.':
                if eSeen or pointSeen:  # not 12e1.2, not 1.2.1
                    return False
                pointSeen = True
            elif s[i] in ['+', '-']:   # -12  or 12e-12
                if i !=0 and s[i-1] != 'e':
                    return False
            else:
                return False
        
        return numSeen and numAfterE
