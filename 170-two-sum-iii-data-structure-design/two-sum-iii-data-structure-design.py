# -*- coding:utf-8 -*-


# Design and implement a TwoSum class. It should support the following operations: add and find.
#
#
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.
#
#
#
# For example,
#
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
#
#


class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.lists = []
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        
        self.lists.append(number)
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        
        _map = set()
        for i in range(0, len(self.lists)):
            if value - self.lists[i] in _map:
                return True
            _map.add(self.lists[i])
            
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
