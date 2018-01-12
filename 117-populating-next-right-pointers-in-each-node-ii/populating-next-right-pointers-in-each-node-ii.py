# -*- coding:utf-8 -*-


# Follow up for problem "Populating Next Right Pointers in Each Node".
# What if the given tree could be any binary tree? Would your previous solution still work?
#
# Note:
# You may only use constant extra space.
#
#
# For example,
# Given the following binary tree,
#
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
#
#
#
# After calling your function, the tree should look like:
#
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL
#
#


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        
        if not root: return
        stack = [root]
        
        while stack:
            size = len(stack)
            for i in range(0, size):
                node = stack.pop(0)
                if i != size-1:
                    node.next = stack[0]
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                    
