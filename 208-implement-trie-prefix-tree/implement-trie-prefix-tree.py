# -*- coding:utf-8 -*-


#
# Implement a trie with insert, search, and startsWith methods.
#
#
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#


class TrieNode(object):

    def __init__(self, is_word=False):
        
        self.next = {}
        self.is_word = is_word


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """

        index = 0
        node = self.root
        while index < len(word):
            chr = word[index]
            if chr not in node.next:
                new_node = TrieNode()
                node.next[chr] = new_node

            node = node.next[chr]
            index += 1
        
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        index = 0
        node = self.root
        while index < len(word):
            chr = word[index]
            if chr not in node.next:
                return False

            node = node.next[chr]
            # if index == len(word) - 1:
                # if node.is_word == False:
                    # return False

            index += 1
        return node.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        index = 0
        node = self.root
        while index < len(prefix):
            chr = prefix[index]
            if chr not in node.next:
                return False
            node = node.next[chr]
            index += 1
        return True

