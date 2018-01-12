# -*- coding:utf-8 -*-


#
# Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.
#
#
# All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".
#
# Example 1:
#
# s = "aabbcc", k = 3
#
# Result: "abcabc"
#
# The same letters are at least distance 3 from each other.
#
#
#
# Example 2:
#
# s = "aaabc", k = 3 
#
# Answer: ""
#
# It is not possible to rearrange the string.
#
#
#
# Example 3:
#
# s = "aaadbbcc", k = 2
#
# Answer: "abacabcd"
#
# Another possible answer is: "abcabcda"
#
# The same letters are at least distance 2 from each other.
#
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all test cases.


class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        # time: O(n), space: O(1)

        def findIndex(index):
            _max = 0
            res = -1
            for j in range(0, 26):
                if count[j] > _max and valid[j] <= i:
                    _max = count[j]
                    res = j
            if res == -1: return -1
            count[res] -= 1
            valid[res] = i + k
            return res
        
        count = [0]*26
        valid = [0]*26
        
        for i in range(0, len(s)):
            count[ord(s[i])-97] +=1
               
        res = ""
        for i in range(0, len(s)):
            idx = findIndex(i)
            if idx == -1: return ""
            res += chr(idx+97)
        
        return res
        
        # priority queue
