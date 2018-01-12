# -*- coding:utf-8 -*-


# Print a binary tree in an m*n 2D string array following these rules: 
#
#
# The row number m should be equal to the height of the given binary tree.
# The column number n should always be an odd number.
# The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them. 
# Each unused space should contain an empty string "".
# Print the subtrees following the same rules.
#
#
# Example 1:
#
# Input:
#      1
#     /
#    2
# Output:
# [["", "1", ""],
#  ["2", "", ""]]
#
#
#
#
# Example 2:
#
# Input:
#      1
#     / \
#    2   3
#     \
#      4
# Output:
# [["", "", "", "1", "", "", ""],
#  ["", "2", "", "", "", "3", ""],
#  ["", "", "4", "", "", "", ""]]
#
#
#
# Example 3:
#
# Input:
#       1
#      / \
#     2   5
#    / 
#   3 
#  / 
# 4 
# Output:
#
# [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
#  ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
#  ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
#  ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
#
#
#
# Note:
# The height of binary tree is in the range of [1, 10].
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        
        def getHeight(root):
            
            if not root:
                return 0
            
            return max(getHeight(root.left), getHeight(root.right)) + 1
        
        def printBT(root, start, end, h, res):
            
            res[h][(start+end)/2] = str(root.val)
            if root.left:
                printBT(root.left, start, (start+end)/2-1, h+1, res)
            if root.right:
                printBT(root.right, (start+end)/2+1, end, h+1, res)    
            
            return 
            
        row = getHeight(root)
        col = 2**row - 1
        res = [["" for j in range(col)] for i in range(row)]
        res[0][col/2] = str(root.val)
        if root.left:
            printBT(root.left, 0, col/2-1, 1, res)
        if root.right:
            printBT(root.right, col/2+1, col-1, 1, res)
        
        return res
    
