# -*- coding:utf-8 -*-


#
# Given a binary tree, return all root-to-leaf paths.
#
#
# For example, given the following binary tree:
#
#
#
#    1
#  /   \
# 2     3
#  \
#   5
#
#
#
# All root-to-leaf paths are:
# ["1->2->5", "1->3"]
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        res = []
        
        def robot(root, _str):
            
            _str = _str+'->'+str(root.val) if _str else str(root.val)
            if not root.left and not root.right:
                res.append(_str)
                return
            
            if root.left:
                robot(root.left, _str)
            if root.right:
                robot(root.right, _str)
        
        if not root: return []
        robot(root, "")
        return res
                
