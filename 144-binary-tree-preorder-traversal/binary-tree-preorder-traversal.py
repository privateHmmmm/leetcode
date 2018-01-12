# -*- coding:utf-8 -*-


# Given a binary tree, return the preorder traversal of its nodes' values.
#
#
# For example:
# Given binary tree [1,null,2,3],
#
#    1
#     \
#      2
#     /
#    3
#
#
#
# return [1,2,3].
#
#
# Note: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root == None: return []
        
        lists = []
        stack = [root]
        while stack:
            cur_node = stack.pop()
            lists.append(cur_node.val)
            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.left:
                stack.append(cur_node.left)
            	# stack.insert(0, cur_node.left)
            # if cur_node.right:
                # if cur_node.left:
                	# stack.insert(1, cur_node.right)
                # else:
                    # stack.insert(0, cur_node.right)
            
        return lists
        
        
        
