# -*- coding:utf-8 -*-


# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
#
#
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
#


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        if len(s) < len(p): return []
        
        cntP = collections.Counter(p)
        cntS = collections.Counter()
        
        res = []
        start, end = 0, 0
        while end < len(s):
            if s[end] not in cntP:
                end += 1
                start = end
                cntS.clear()
                continue
            else:
                cntS[s[end]] +=1
            
            end += 1
            if end - start == len(p) and cntP == cntS:
                res.append(start)
            
            # end += 1
            if end - start >= len(p):
                cntS[s[start]] -= 1
                if cntS[s[start]] == 0: del cntS[s[start]]
                start += 1
        
        return res
