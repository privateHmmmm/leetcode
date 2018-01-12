# -*- coding:utf-8 -*-


# Given a binary tree, count the number of uni-value subtrees.
# A Uni-value subtree means all nodes of the subtree have the same value.
#
#
# For example:
# Given binary tree,
#
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
#
#
#
# return 4.
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.ans = 0
        
        def helper(root):
            
            if not root: return True
            
            left = helper(root.left)
            right = helper(root.right)
            
            if left and right:
                if root.left and root.left.val != root.val:
                    return False
                
                if root.right and root.right.val != root.val:
                    return False
            
                self.ans +=1
                return True

            return False
        
        helper(root)
        return self.ans
        
