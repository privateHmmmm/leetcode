# -*- coding:utf-8 -*-


#
# Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place. 
#
#
#
# The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.
#
#
# Example 1:
#
# Input: "UD"
# Output: true
#
#
#
# Example 2:
#
# Input: "LL"
# Output: false
#
#


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        """
        UD=0
        LR=0
        for i in range(0, len(moves)):
            if moves[i]=='U':
                UD+=1
            elif moves[i]=='D':
                UD-=1
            elif moves[i]=='L':
                LR+=1
            else:
                LR-=1
        
        return (not UD and not LR)
        """
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
