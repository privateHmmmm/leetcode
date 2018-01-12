# -*- coding:utf-8 -*-


# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
#
# For example:
# Given the following binary tree,
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
#
#
#
# You should return [1, 3, 4].
#
#
# Credits:Special thanks to @amrsaqr for adding this problem and creating all test cases.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root: return []
        res = []
        queue = [root]
        
        while queue:
            size = len(queue)
            for i in range(0, size):
                node = queue.pop(0)
                if i == size-1: res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return res
    
