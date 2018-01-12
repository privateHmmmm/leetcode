# -*- coding:utf-8 -*-


#
# Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.
#
# Note:
#
# Given target value is a floating point.
# You may assume k is always valid, that is: k &le; total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
#
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        
        # time: O(n) space: O(n)
        res = []
        def helper(root):
            if root == None: return
            helper(root.left)
            if len(res) == k and abs(res[0] - target) > abs(root.val-target):
                res.remove(res[0])
            if len(res) < k: res.append(root.val)
            helper(root.right)
        
        helper(root)
        return res
    
    # TODO look at other method 
        
