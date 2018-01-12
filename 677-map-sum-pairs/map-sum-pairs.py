# -*- coding:utf-8 -*-


#
# Implement a MapSum class with insert, and sum methods.
#
#
#
# For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.
#
#
#
# For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.
#
#
# Example 1:
#
# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5
#
#
#


class TrieNode(object):

    def __init__(self, value=False):
        
        self.children = {}
        # self.is_word = False
        self.value = value
        
    
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.root = TrieNode()
        
        
    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        
        node = self.root
        index = 0
        while index<len(key):
            if key[index] not in node.children:
                node.children[key[index]] = TrieNode()
            node = node.children[key[index]]
            index +=1
        node.value = val    
        
    def NodeSum(self, node):
        
        Sum = node.value if node.value != False else 0
        # Sum = 0

        for c in node.children:
            # if node.children[c].value != False: Sum += node.children[c].value
            Sum +=self.NodeSum(node.children[c])
        
        return Sum

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        
        node = self.root
        index = 0
        while index < len(prefix):
            if prefix[index] in node.children:
                node = node.children[prefix[index]]
            else:
                node = None
                break
            index +=1
    
        return self.NodeSum(node) if node else 0
        

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
