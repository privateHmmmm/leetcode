# -*- coding:utf-8 -*-


# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
#
# Note: The length of path between two nodes is represented by the number of edges between them.
#
#
# Example 1:
#
#
#
#
# Input:
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
#
#
#
#
# Output:
#
# 2
#
#
#
#
# Example 2:
#
#
#
#
# Input:
#
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
#
#
#
#
# Output:
#
# 2
#
#
#
# Note:
# The given binary tree has not more than 10000 nodes.  The height of the tree is not more than 1000.
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        self.max = 0
        def helper(root):
            
            if not root: return 0
            
            res = 0
            left_lens = helper(root.left)
            right_lens = helper(root.right)
            root_lens = 0
            
            if root.left and root.left.val == root.val:
                root_lens += (left_lens + 1)
                res = left_lens + 1
            if root.right and root.right.val == root.val:
                root_lens += (right_lens + 1)
                res = max(res, right_lens + 1)
            self.max = max(self.max, root_lens)
            # return root_lens # !!!! NOT THIS
            return res
        
        helper(root)
        return self.max
    
