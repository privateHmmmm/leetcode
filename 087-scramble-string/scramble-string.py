# -*- coding:utf-8 -*-


#
# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
#
#
# Below is one possible representation of s1 = "great":
#
#
#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
#
#
# To scramble the string, we may choose any non-leaf node and swap its two children.
#
#
# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
#
#
#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
#
#
# We say that "rgeat" is a scrambled string of "great".
#
#
# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
#
#
#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
#
#
# We say that "rgtae" is a scrambled string of "great".
#
#
# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
#


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
    
        n, m = len(s1), len(s2)
        if n != m:
            return False
        
        count={}
        for i in range(0, n):
            if s1[i] in count:
                count[s1[i]]+=1
            else:
                count[s1[i]]=1
            if s2[i] in count:
                count[s2[i]]-=1
            else:
                count[s2[i]]=-1
                
        for i in count:
            if count[i]!=0:
                return False
        
        if n < 4 or s1 == s2:
            return True
        f = self.isScramble
        for i in range(1, n):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                return True
        return False
