# -*- coding:utf-8 -*-


#
# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
#
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
#
#
# For example,
# Given words = ["oath","pea","eat","rain"] and board = 
#
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
#
#
# Return ["eat","oath"].
#
#
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#
#
# click to show hint.
#
# You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
#
# If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.
#


class TreeNode(object):
    
    def __init__(self):
        
        self.children = {}
        self.word = None

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        n = len(board)
        if n == 0: return False
        m = len(board[0])
        if m == 0: return False
        ans = []
            
        def visit(i, j, root):
            
            if root == None or board[i][j] not in root.children:
                return
            
            save = board[i][j]
            root = root.children[board[i][j]]
            board[i][j] = "#"
            if root.word:
                ans.append(root.word)    
                root.word = None    # !!!!
            
            for s in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newI = i + s[0]
                newJ = j + s[1]
                if 0<=newI<n and 0<=newJ<m:
                    visit(newI, newJ, root)
           
            board[i][j] = save
        
        def insert(root, word):
            
            for i in range(0, len(word)):
                if word[i] not in root.children:
                    root.children[word[i]] = TreeNode()
                root = root.children[word[i]]
            root.word = word
                
        root = TreeNode()
        for word in words:
            insert(root, word)
        
        for i in range(0, n):
            for j in range(0, m):
                visit(i, j, root)
        
        return ans
        
