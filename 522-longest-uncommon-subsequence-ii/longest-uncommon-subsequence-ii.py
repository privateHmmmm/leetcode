# -*- coding:utf-8 -*-


#
# Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.
#
#
#
# A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.
#
#
#
# The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.
#
#
# Example 1:
#
# Input: "aba", "cdc", "eae"
# Output: 3
#
#
#
# Note:
#
# All the given strings' lengths will not exceed 10.
# The length of the given list will be in the range of [2, 50].
#
#


class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        
        def subseq(s1, s2):
            # return True if s1 is a subseqence of s2
            # if len(s1) > len(s2):
                # return False
            # elif len(s1) == len(s2):
                # return s1==s2
            # else:
                # index=-1
                # print 'sss %s, %s' %(s1, s2)
                # for i in range(0, len(s1)):
                    # if s1[i] in s2[index+1:]:
                        # index=s2[index+1:].index(s1[i])
                        # print index
                    # else:
                        # return False
                # return True
            
            i = 0
            for c in s2:
                if i<len(s1) and c == s1[i]:
                    i+=1
            
            return i == len(s1)
            
        strs.sort(key=len, reverse=True)
        for i in range(0, len(strs)):
            # print i
            for j in range(0, len(strs)):
                if i == j:
                    continue
                else:
                    if subseq(strs[i], strs[j])==True:
                        break
            else:
                return len(strs[i])
        
        return -1
            
