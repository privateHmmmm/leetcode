# -*- coding:utf-8 -*-


# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        def helper(iStart, iEnd, pStart, pEnd):
            
            if iStart>iEnd or pStart>pEnd:
                return None
            
            root = TreeNode(postorder[pEnd])
            left_num = inorder[iStart:iEnd+1].index(postorder[pEnd])
            right_num = iEnd - iStart - left_num
            root.left = helper(iStart, iStart+left_num-1, pStart, pStart+left_num-1)
            root.right = helper(iStart+left_num+1, iEnd, pStart+left_num, pEnd-1)
            return root
        
        return helper(0, len(inorder)-1, 0, len(postorder)-1)
    
