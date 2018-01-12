# -*- coding:utf-8 -*-


#
# Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.
#
#
# Example 1:
#
# Input: 
#     1
#    / \
#   0   2
#
#   L = 1
#   R = 2
#
# Output: 
#     1
#       \
#        2
#
#
#
# Example 2:
#
# Input: 
#     3
#    / \
#   0   4
#    \
#     2
#    /
#   1
#
#   L = 1
#   R = 3
#
# Output: 
#       3
#      / 
#    2   
#   /
#  1
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        
        def trim(root):
            
            if not root:
                return None
            
            # if root.val < L:
                # find right
                # root = root.right
                # while root:
                    
                    
                    
                    # if root.val >= L:
                        # break
                    # else:
                        # root = root.right
            if root.val > R or root.val < L:
                # find left
                # root = root.left
                while root:
                    if root.val > R:
                        root = root.left
                    elif root.val < L:
                        root = root.right
                    else:
                        break
                    
                    # if root.val <= R and root.val >=L:
                        # print root.val
                        # break
                    # else:
                        # root = root.left
                
            if not root:
                return None
            root.left=trim(root.left)
            root.right=trim(root.right)
            return root
        
        return trim(root)
            
            
            
            
            
        
