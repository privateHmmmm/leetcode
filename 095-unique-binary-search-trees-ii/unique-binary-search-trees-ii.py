# -*- coding:utf-8 -*-


# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.
#
#
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.
#
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
    
        def robot(start, end):
            
            lists = []
            if start > end:
                lists.append(None)
                
            for i in range(start, end+1):
                lefts = robot(start, i-1)
                rights = robot(i+1, end)
                for left in lefts:
                    for right in rights:
                        root = TreeNode(i)   # Don't write into ListNode again!!!
                        root.left = left
                        root.right = right
                        lists.append(root)
            
            return lists
        
        if n == 0: return []
        return robot(1, n)
     
