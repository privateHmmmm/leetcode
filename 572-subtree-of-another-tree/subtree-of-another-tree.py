# -*- coding:utf-8 -*-


#
# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
#
#
# Example 1:
#
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#
# Given tree t:
#
#    4 
#   / \
#  1   2
#
# Return true, because t has the same structure and node values with a subtree of s.
#
#
# Example 2:
#
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
#
# Given tree t:
#
#    4
#   / \
#  1   2
#
# Return false.
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        
        
        def cmpTree(root, t):
            
            if not t and not root:
                return True
            elif (not t and root) or (not root and t):
                return False
            
            if root.val == t.val:
                if cmpTree(root.left, t.left) and cmpTree(root.right, t.right):
                    return True
            return False
                
        queue = [s]
        while queue:
            node = queue.pop(0)
            if True == cmpTree(node, t):
                return True
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return False
