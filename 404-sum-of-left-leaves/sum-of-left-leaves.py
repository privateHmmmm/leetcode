# -*- coding:utf-8 -*-


# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        """
        # DFS
        if not root: return 0
        
        Sum = 0
        if root.left and root.left.left == None and root.left.right == None:
            Sum += root.left.val 
        
        left_sum = self.sumOfLeftLeaves(root.left)
        right_sum = self.sumOfLeftLeaves(root.right)
        
        return Sum + left_sum + right_sum
        """
        
        if not root: return 0
        queue = [root]
        res = 0
        
        while queue:
            node = queue.pop(0)
            if node.left:
                if not node.left.left and not node.left.right:
                    res += node.left.val
                elif node.left:
                    queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
            
        return res
    
