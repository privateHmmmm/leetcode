# -*- coding:utf-8 -*-


# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
#
# Calling next() will return the next smallest number in the BST.
#
# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree. 
#
# Credits:Special thanks to @ts for adding this problem and creating all test cases.


# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        
        self.cur = root
        self.stack = []

    def hasNext(self):
        """
        :rtype: bool
        """
        
        if self.stack or self.cur: 
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
        
        cur = self.cur
        while cur:
            self.stack.append(cur)
            cur = cur.left
        
        cur = self.stack.pop()
        res = cur.val
        self.cur = cur.right
        return res
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
