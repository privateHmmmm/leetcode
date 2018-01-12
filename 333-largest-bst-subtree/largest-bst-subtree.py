# -*- coding:utf-8 -*-


# Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.
# Note:
# A subtree must include all of its descendants.
# Here's an example:
#
#     10
#     / \
#    5  15
#   / \   \ 
#  1   8   7
#
# The Largest BST Subtree in this case is the highlighted one. 
# The return value is the subtree's size, which is 3. 
#
#
#
# Follow up:
# Can you figure out ways to solve it with O(n) time complexity?
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        self.max = 0
        
        def helper(root):
            
            root_lens, root_min, root_max = 1, root.val, root.val
            
            left_flag, right_flag = True, True
            if root.left:
                left_lens, left_min, left_max = helper(root.left)
                if left_max < root.val:
                    root_lens += left_lens
                    root_min = left_min
                else:
                    left_flag = False

            if root.right:
                right_lens, right_min, right_max = helper(root.right)
                if right_min > root.val:
                    root_lens += right_lens
                    root_max = right_max
                else:
                    right_flag = False
            
            if left_flag and right_flag:
                self.max = max(self.max, root_lens)
                return root_lens, root_min, root_max
            else:
                return 0, -2**31, 2**31-1
        
        if not root: return 0
        helper(root)
        return self.max
        
