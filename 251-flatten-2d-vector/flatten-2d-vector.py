# -*- coding:utf-8 -*-


#
# Implement an iterator to flatten a 2d vector.
#
#
# For example,
# Given 2d vector = 
#
# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]
#
#
#
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].
#
#
#
# Follow up:
# As an added challenge, try to code it using only iterators in C++ or iterators in Java.
#


class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.nextI, self.nextJ = 0, 0   
        self.vec = vec2d
    
    def next(self):
        """
        :rtype: int
        """
        
        self.nextJ += 1
        return self.vec[self.nextI][self.nextJ-1]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        
        if self.nextI >= len(self.vec):
            return False
        
        while self.nextJ >= len(self.vec[self.nextI]):
            self.nextI += 1
            self.nextJ = 0
            if self.nextI >= len(self.vec):
                return False
        
        return True
            

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
