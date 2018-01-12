# -*- coding:utf-8 -*-


#
# You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.
#
#
#
# Write a function to determine if the starting player can guarantee a win.
#
#
#
# For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".
#
#
# Follow up:
# Derive your algorithm's runtime complexity.
#


class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # time: O(2^n)
        
        _map = {}
        
        def helper(s):
            
            if s in _map: return _map[s]
            
            for i in range(0, len(s)-1):
                if s[i] == '+' and s[i+1] == '+':
                    if False == helper(s[:i]+'--'+s[i+2:]):
                        _map[s] = True
                        return True
            
            _map[s] = False
            return False
        
        return helper(s)
        
