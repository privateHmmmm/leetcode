# -*- coding:utf-8 -*-


# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
#
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
#
# For example:
# Given BST [1,null,2,2],
#
#    1
#     \
#      2
#     /
#    2
#
#
#
# return [2].
#
#
# Note:
# If a tree has more than one mode, you can return them in any order.
#
#
# Follow up:
# Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        """
        # This is wrong, for example: [6,2,8,0,4,7,9,null,null,2,6]
        _max = [0]
        res = []
        
        def _mode(root):
            
            if root == None:
                return 0
            
            tmp = 1
            left_cnt = _mode(root.left)
            right_cnt = _mode(root.right)
            
            if root.left and root.val == root.left.val:
                tmp += left_cnt
            if root.right and root.val == root.right.val:
                tmp += right_cnt
            
            if tmp == _max[0]:
                res.append(root.val)
            elif tmp > _max[0]:
                _max[0] = tmp
                res[:] = [root.val]
            
            return tmp
        
        _mode(root)
        return res
        """
        
        if not root: return []
        _inorder = []
        
        def inorder(root):
            
            if root == None:
                return
            
            inorder(root.left)
            _inorder.append(root.val)
            inorder(root.right)
        
        inorder(root)
        res = []
        cnt = collections.Counter(_inorder)
        _max = max(cnt.values())
        for k, v in cnt.iteritems():
            if v == _max:
                res.append(k)
        return res
        
