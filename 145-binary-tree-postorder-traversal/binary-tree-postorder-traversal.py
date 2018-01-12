# -*- coding:utf-8 -*-


# Given a binary tree, return the postorder traversal of its nodes' values.
#
#
# For example:
# Given binary tree {1,#,2,3},
#
#    1
#     \
#      2
#     /
#    3
#
#
#
# return [3,2,1].
#
#
# Note: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class StackNode(object):
    
    def __init__(self, root, is_first=True):
        
        self.root = root
        self.is_first = is_first
        
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root == None: return []
        
        lists = []
        stack = [root]
        
        while stack:
            cur = stack.pop()
            lists.insert(0, cur.val)

            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
                    
        return lists
        
#         while stack or root != None:
#             while root != None:
#                 snode = StackNode(root)
#                 stack.append(snode)
#                 root = root.left
            
#             if stack:
#                 snode = stack.pop()
#                 if snode.is_first == True:
#                     snode.is_first = False
#                     stack.append(snode)
#                     root = snode.root.right
#                 else:
#                     lists.append(snode.root.val)
#                     root = None
        
#         return lists
                
