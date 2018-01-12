# -*- coding:utf-8 -*-


#
# Two elements of a binary search tree (BST) are swapped by mistake.
#
# Recover the tree without changing its structure.
#
#
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        # inorder
        
        pre = [None]
        first = [None]
        second = [None]
        
        def helper(root):
            
            if not root: return
            helper(root.left)
            if (pre[0] and pre[0].val >= root.val):
                if first[0] == None:
                    first[0] = pre[0]  # !!!!
                second[0] = root  # !!!
            pre[0] = root
            helper(root.right)
        
        helper(root)
        tmp = first[0].val
        first[0].val = second[0].val
        second[0].val = tmp
    
        
    
