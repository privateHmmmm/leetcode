# -*- coding:utf-8 -*-


#
# Design a data structure that supports the following two operations:
#
#
# void addWord(word)
# bool search(word)
#
#
#
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
#
#
# For example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
#
#
#
# Note:
# You may assume that all words are consist of lowercase letters a-z.
#
#
# click to show hint.
#
# You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first.
#


class TrieNode(object):
    
    def __init__(self, is_word=False):
        
        self.next={}
        self.is_word=is_word

class Trie(object):
    
    def __init__(self):
        
        self.root=TrieNode(False)
        
    @classmethod
    def DFS(cls, word, node):
        
        if word=="":
            return node.is_word
        
        index=0
        
        while index < len(word):
            if word[index]==".":
                for n in node.next:
                    res = cls.DFS(word[index+1:], node.next[n])
                    if res == True:
                        return True
                return False
            elif word[index] not in node.next:
                return False
            
            node=node.next[word[index]]
            index +=1
            
        return node.is_word
        
        
    def search(self, word):
        
        return Trie.DFS(word, self.root)
    
    def insert(self, word):
        
        index=0
        node=self.root
    
        while index < len(word):
            is_word=True if index==len(word)-1 else False
            if word[index] not in node.next:
                new_node=TrieNode(is_word)
                node.next[word[index]]=new_node
            else:
                if is_word == True:
                    node.next[word[index]].is_word=True
        
            node=node.next[word[index]]
            index +=1

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.trie.insert(word)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        
        return self.trie.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
