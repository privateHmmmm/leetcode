# -*- coding:utf-8 -*-


# Given preorder and inorder traversal of a tree, construct the binary tree.
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        def build(st1, ed1, st2, ed2):
            
            if st1 > ed1:
                return None
            
            find = inorder.index(preorder[st1], st2)
            if find == -1:
                return None
            
            c = find-st2 # left tree node num
            
            r = TreeNode(preorder[st1])
            r.left = build(st1+1, st1+c, st2, find-1)  
            r.right = build(st1+c+1, ed1, find+1, ed2)
            return r
        
        return build(0, len(preorder)-1, 0, len(inorder)-1)
        
        
