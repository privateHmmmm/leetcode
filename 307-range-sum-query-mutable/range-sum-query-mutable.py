# -*- coding:utf-8 -*-


# Given an integer array nums, find the sum of the elements between indices i and j (i &le; j), inclusive.
#
# The update(i, val) function modifies nums by updating the element at index i to val.
#
# Example:
#
# Given nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
#
#
#
# Note:
#
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is distributed evenly.
#
#


# import copy
class TreeNode(object):
    
    def __init__(self):
        
        self.st = 0
        self.ed = 0
        self._sum = 0
    
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        
        if not nums:
            depth = 0
        else:
            depth = int(math.log(len(nums), 2)) + 2
        total = 2**depth - 1
        self.nums = nums
        self.indexes = [0] *len(nums)
        self.tlist = [TreeNode() for i in range(0, total)]
        # self.start = 2**(depth-1)-1
        # print total, self.start
        self.buildTree(0, 0, len(nums)-1)
        # for i in range(0, len(self.tlist)):
            # print self.tlist[i].st, self.tlist[i].ed, self.tlist[i]._sum
        

    def buildTree(self, id, st, ed):
        
        if id >= len(self.tlist):
            return 
        
        self.tlist[id].st = st
        self.tlist[id].ed = ed
        
        if st <= ed:
            if st == ed:
                self.tlist[id]._sum = self.nums[st]
                self.indexes[st] = id
            else:
                mid = (st+ed)/2
                # [st, mid]
                self.buildTree(2*id+1, st, mid)
                # [mid+1, ed]
                self.buildTree(2*id+2, mid+1, ed)
                self.tlist[id]._sum = self.tlist[2*id+1]._sum + self.tlist[2*id+2]._sum
        else:
            self.tlist[id]._sum = 0
            
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        
        id = self.indexes[i]
        # print id
        diff = val - self.nums[i]
        
        if diff != 0:
            self.nums[i] = val
            while id>=0:
                self.tlist[id]._sum += diff
                id = (id+1)/2-1
            
        
    def getSum(self, id, want_st, want_ed):
        
        if id < len(self.tlist):
            if self.tlist[id].st >= want_st and self.tlist[id].ed <= want_ed:
                return self.tlist[id]._sum
            elif self.tlist[id].st > want_ed or self.tlist[id].ed < want_st:
                return 0
            # elif self.tlist
            
            else:
                return self.getSum(2*id+1, want_st, want_ed) + self.getSum(2*id+2, want_st, want_ed)
        else:
            return 0

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        
        if i==j and i<len(self.nums): return self.nums[i]
        return self.getSum(0, i, j)
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
