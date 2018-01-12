# -*- coding:utf-8 -*-


# Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.
#
#
#
# Example:
# Given binary tree 
#
#           1
#          / \
#         2   3
#        / \     
#       4   5    
#
#
#
# Returns [4, 5, 3], [2], [1].
#
#
#
# Explanation:
#
# 1. Removing the leaves [4, 5, 3] would result in this tree:
#
#           1
#          / 
#         2          
#
#
#
# 2. Now removing the leaf [2] would result in this tree:
#
#           1          
#
#
#
# 3. Now removing the leaf [1] would result in the empty tree:
#
#           []         
#
#
#
#
# Returns [4, 5, 3], [2], [1].
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all test cases.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        # 把每个节点放在res self depth位置
        res = []
        def helper(root):
            
            if not root: return -1
            depth = max(helper(root.left), helper(root.right)) + 1
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            return depth
            
        helper(root)
        return res
            
            
