# -*- coding:utf-8 -*-


# Given a complete binary tree, count the number of nodes.
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def getHeight(root):
            
            res = 0
            while root:
                res += 1
                root = root.left
            return res
        
        def getCount(root):
            
            height = getHeight(root)
            if height <= 1: return height
            
            if getHeight(root.right) == height - 1:
                return 2**(height-1)+getCount(root.right)
            else:
                return getCount(root.left) + 2**(height-2)
        
        return getCount(root)
                
                
        
