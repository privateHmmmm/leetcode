# -*- coding:utf-8 -*-


# Find the total area covered by two rectilinear rectangles in a 2D plane.
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
#
#
#
#
# Assume that the total area is never beyond the maximum possible value of int.
#
#
# Credits:Special thanks to @mithmatt for adding this problem, creating the above image and all test cases.


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        
        left = max(A, E)
        right = min(C, G)
        bottom = max(B, F)
        top = min(D, H)
        
        overlap = 0
        if left < right and bottom < top:
            overlap = (right-left)*(top-bottom)
        
        return (C-A)*(D-B) + (G-E)*(H-F) - overlap
