# -*- coding:utf-8 -*-


# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
#
# Basically, the deletion can be divided into two stages:
#
# Search for a node to remove.
# If the node is found, delete the node.
#
#
#
# Note: Time complexity should be O(height of tree).
#
# Example:
#
# root = [5,3,6,2,4,null,7]
# key = 3
#
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Given key to delete is 3. So we find the node with value 3 and delete it.
#
# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
#
#     5
#    / \
#   4   6
#  /     \
# 2       7
#
# Another valid answer is [5,2,6,null,4,null,7].
#
#     5
#    / \
#   2   6
#    \   \
#     4   7
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        
        def _find(root, key):
            
            if root == None: return None, None
            parent = None
            while root:
                if root.val == key:
                    return parent, root 
                elif root.val > key:
                    parent, root = root, root.left
                else:
                    parent, root = root, root.right
            
            return None, None
        
        def _deleteLeaf(parent, node):
            
            if parent == None:
                return None
            
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
            return root
        
        def _deleteSingleSon(parent, node):
            
            son = node.left if node.left else node.right
            
            if parent == None:
                return son
            
            if parent.left == node:
                parent.left = son
            else:
                parent.right = son
            return root
            
        def _deleteTwoSon(node):
            
            p1 = node
            tmp = node.right
            while tmp.left:
                p1 = tmp
                tmp = tmp.left
            
            # print tmp.val
            if tmp.right == None:
                _deleteLeaf(p1, tmp)
            else:
                _deleteSingleSon(p1, tmp)
            node.val = tmp.val
                
        parent, node = _find(root, key)
        print parent.val if parent else None, node.val if node else None
        if node == None:
            return root
        
        if node.left == None and node.right == None:
            return _deleteLeaf(parent, node)
        elif not node.left or not node.right:
            return _deleteSingleSon(parent, node)
        else:
            _deleteTwoSon(node)
            return root

