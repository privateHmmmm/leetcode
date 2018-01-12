# -*- coding:utf-8 -*-


#
# Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.
#
#
# For example:
# Given a binary tree {1,2,3,4,5},
#
#     1
#    / \
#   2   3
#  / \
# 4   5
#
#
#
# return the root of the binary tree [4,5,2,#,#,3,1].
#
#    4
#   / \
#  5   2
#     / \
#    3   1  
#
#
#
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
#
# OJ's Binary Tree Serialization:
#
# The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.
#
#
# Here's an example:
#
#    1
#   / \
#  2   3
#     /
#    4
#     \
#      5
#
# The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}". 
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        #          1                      1 
        #        /   \                  /
        #       2     3       ----->   2 --- 3     
        #     /   \                  /
        #    4     5                4 --- 5
        #
        
        if not root or (not root.left and not root.right):
            return root
        
        newRoot = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
        return newRoot
    
    
