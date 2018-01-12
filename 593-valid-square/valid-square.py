# -*- coding:utf-8 -*-


# Given the coordinates of four points in 2D space, return whether the four points could construct a square.
#
# The coordinate (x,y) of a point is represented by an integer array with two integers.
#
# Example:
#
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True
#
#
#
#  Note: 
#
# All the input integers are in the range [-10000, 10000].
# A valid square has four equal sides with positive length and four equal angles (90-degree angles).
# Input points have no order.
#
#


class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        
        
        vector12 = [p2[0]-p1[0], p2[1]-p1[1]]
        vector13 = [p3[0]-p1[0], p3[1]-p1[1]]
        vector14 = [p4[0]-p1[0], p4[1]-p1[1]]
        
        iP213 = vector12[0]*vector13[0] + vector12[1]*vector13[1]  # inner product
        iP214 = vector12[0]*vector14[0] + vector12[1]*vector14[1]
        iP314 = vector13[0]*vector14[0] + vector13[1]*vector14[1]
        
        test = [iP213, iP214, iP314]
        
        if 0 in [iP213, iP214, iP314]:
            test.remove(0)
            if test[0] == test[1] and test[0] > 0:
                return True
            
        return False
    
