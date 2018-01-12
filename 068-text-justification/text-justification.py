# -*- coding:utf-8 -*-


#
# Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
#
#
#
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.
#
#
#
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
#
#
#
# For the last line of text, it should be left justified and no extra space is inserted between words.
#
#
#
# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.
#
#
#
# Return the formatted lines as:
#
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
#
#
#
#
# Note: Each word is guaranteed not to exceed L in length.
#
#
#
# click to show corner cases.
#
# Corner Cases:
#
#
# A line other than the last line might contain only one word. What should you do in this case?
# In this case, that line should be left-justified.
#
#


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
        res = []
        index = 0
        while index < len(words):
            count = len(words[index])
            last = index + 1
            while last < len(words): 
                if count + 1 + len(words[last]) > maxWidth: break
                count += (1 + len(words[last]))
                last += 1
            word_num = last - index 
            _str = words[index]
            if last == len(words) or word_num == 1: #For the last line of text, it should be left ...
                for i in range(index+1, last):
                    _str += (' ' + words[i])
                _str += (' ' * (maxWidth - len(_str)))
            else:
                total_space = (maxWidth - count)
                space = total_space/(word_num-1) 
                remain = total_space % (word_num-1)
                for i in range(index+1, last):
                    if remain > 0:
                        _str += ' '
                        remain -= 1
                    _str += (' '*space + ' ' + words[i])
            res.append(_str)
            index = last
        return res
            
