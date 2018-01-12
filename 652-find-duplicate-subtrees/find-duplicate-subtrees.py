# -*- coding:utf-8 -*-


#
# Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them. 
#
#
# Two trees are duplicate if they have the same structure with same node values.
#
#
# Example 1: 
#
#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
#
# The following are two duplicate subtrees:
#
#       2
#      /
#     4
#
# and
#
#     4
#
# Therefore, you need to return above trees' root in the form of a list.
#
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        
        def trav(root):
            if not root:    return 'null'
            hashstring = '%s,%s,%s' % (str(root.val), trav(root.left), trav(root.right))    # inorder
            nodes[hashstring].append(root)
            return hashstring
            
        nodes = collections.defaultdict(list)
        trav(root)
        # print nodes
        return [nodes[hashstring][0] for hashstring in nodes if len(nodes[hashstring])>1]
            
            
            
