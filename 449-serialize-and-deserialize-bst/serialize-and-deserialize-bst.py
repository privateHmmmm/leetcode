# -*- coding:utf-8 -*-


# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment. 
#
# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.
#
#
# The encoded string should be as compact as possible.
#
#
#
# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if not root:
            return ""
        
        ino_list = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            ino_list.append(str(root.val))
            inorder(root.right)
        inorder(root)
        
        preo_list = []
        def preorder(root):
            if not root:
                return 
            preo_list.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        
        return " ".join(ino_list) + " " + " ".join(preo_list)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data:
            return None
        
        tmp = data.split(" ")
        ino_list = tmp[:len(tmp)/2]
        preo_list = tmp[len(tmp)/2:]
        
        def constructTreeFromInorderPreorder(ino_list, preo_list):            
            if not preo_list:
                return None
            
            root = TreeNode(preo_list[0])
            idx = ino_list.index(preo_list[0])
            ino_left = ino_list[:idx]
            ino_right = ino_list[idx+1:]
            preo_left = preo_list[1:idx+1]
            preo_right = preo_list[idx+1:]
            
            root.left = constructTreeFromInorderPreorder(ino_left, preo_left)
            root.right = constructTreeFromInorderPreorder(ino_right, preo_right)
            return root
        
        return constructTreeFromInorderPreorder(ino_list, preo_list)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
